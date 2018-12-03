import sys
import time
import log.client_log_config
import logging
from socket import socket, AF_INET, SOCK_STREAM
from errors import UsernameTooLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from JIM.config import *
from JIM.utils import send_message, get_message

logger = logging.getLogger('client_log')


def create_presence(account_name="Guest"):
    if not isinstance(account_name, str):
        logger.warning("TypeError")
        raise TypeError
    if len(account_name) > 25:
        logger.warning("Имя пользователя {} должно быть не более 26 символов".format(account_name))
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
        logger.warning("TypeError")
        raise TypeError
    if RESPONSE not in response:
        logger.warning('Не хватает обязательного атрибута {}'.format(RESPONSE))
        raise MandatoryKeyError(RESPONSE)
    code = response[RESPONSE]
    if len(str(code)) != 3:
        logger.warning("Неверная длина кода {}. Длина кода должна быть 3 символа.".format(code))
        raise ResponseCodeLenError(code)
    if code not in RESPONSE_CODES:
        logger.warning('Неверный код ответа {}'.format(code))
        raise ResponseCodeError(code)
    return response


# Start client
if __name__ == '__main__':
    logger.info("Запуск скрипта клиента")
    client = socket(AF_INET, SOCK_STREAM)
    logger.info("Создает сокет TCP")
    try:
        addr = sys.argv[1]
        logger.info("Получает IP-адрес: {}".format(addr))
    except IndexError:
        logger.exception(IndexError)
        addr = 'localhost'
        logger.info("Получает IP-адрес: 127.0.0.1")
    try:
        port = int(sys.argv[2])
        logger.info("Получает Порт: {}".format(port))
    except IndexError:
        logger.exception(IndexError)
        port = 7777
        logger.info("Получает Порт: {}".format(port))
    except ValueError:
        # print('Порт должен быть целым числом')
        logger.exception("Порт должен быть целым числом")
        sys.exit(0)

    client.connect((addr, port))
    logger.info("Устанавливает соединение с сервером")
    presence = create_presence()
    logger.info("Сформировывает presence-сообщение")
    send_message(client, presence)
    logger.info("Отправляет сообщение серверу")
    response = get_message(client)
    logger.info("Получает ответ сервера")
    response = translate_message(response)
    logger.info("Обрабатывает сообщение сервера")
    # print(response)
    logger.info("Сообщение сервера - {}".format(response))


