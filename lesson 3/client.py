import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from errors import UsernameTooLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from JIM.config import *
from JIM.utils import send_message, get_message


def create_presence(account_name='Guest'):
    if not isinstance(account_name, str):
        raise TypeError
    if len(account_name) > 25:
        raise UsernameTooLongError(account_name)

    message = {
        ACTION: PRESENCE,
        TIME: time.asctime(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return message


def translate_message(response):
    if not isinstance(response, dict):
        raise TypeError
    if RESPONSE not in response:
        raise MandatoryKeyError
    code = response[RESPONSE]
    if len(str(code)) != 3:
        raise ResponseCodeLenError
    if code not in RESPONSE_CODES:
        raise ResponseCodeError(code)
    return response


# Start client
if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    client.connect((addr, port))
    presence = create_presence()
    send_message(client, presence)
    response = get_message(client)
    response = translate_message(response)
    print(response)

