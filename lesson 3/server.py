import sys
import json
import log.server_log_config
import logging
from socket import socket, AF_INET, SOCK_STREAM
from JIM.utils import get_message, send_message
from JIM.config import *

logger = logging.getLogger('server_log')


def presence_response(presence_message):

    if ACTION in presence_message and presence_message[ACTION] == PRESENCE and TIME in presence_message:
        return {RESPONSE: 200}
    else:
        return {RESPONSE: 400, ERROR: 'Неверный запрос'}


# Start server
if __name__ == '__main__':
    logger.info("Запуск скрипта сервера")
    server = socket(AF_INET, SOCK_STREAM)
    logger.info("Создает сокет TCP")
    try:
        addr = sys.argv[1]
    except IndexError:
        logger.exception(IndexError)
        addr = ''
    try:
        port = int(sys.argv[2])
    except IndexError:
        logger.exception(IndexError)
        port = 7777
    except ValueError:
        # print('Порт должен быть целым числом')
        logger.warning("Порт должен быть целым числом")
        sys.exit(0)

    server.bind((addr, port))
    logger.info("Присваивает порт {}".format(port))
    server.listen(5)
    logger.info("Переходит в режим ожидания запросов")
    while True:
        client, addr = server.accept()
        logger.info("Принимает запрос на установку соединения")
        presence = get_message(client)
        logger.info("Принимает сообщение от клиента")
        logger.info("Полученное сообщение - {}".format(presence))
        response = presence_response(presence)
        logger.info("Формирует ответ клиенту")
        send_message(client, response)
        logger.info("Отправляет ответ клиенту")
        client.close()
        logger.info("Закрывает соединение")
