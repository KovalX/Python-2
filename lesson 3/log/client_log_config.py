import logging

# Создаем логгер - регистратор верхнего уровня
logger = logging.getLogger('client_log')

# Создаем объект Formatter (определяем формат сообщений)
_format = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(message)s")

# Создаем обработчик
fh = logging.FileHandler("client.log", encoding="utf-8")
# Подключаем объект Formatter к обработчику
fh.setFormatter(_format)

# Добавляем обработчик к регистратору
logger.addHandler(fh)
# Определяем уровень важности для обработчика
logger.setLevel(logging.INFO)

