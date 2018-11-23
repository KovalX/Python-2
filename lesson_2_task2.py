'''2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item),
количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных
в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;

Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''

import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {}
    order[u'товар'] = item
    order[u'количество'] = quantity
    order[u'цена'] = price
    order[u'покупатель'] = buyer
    order[u'дата'] = date

    with open('orders.json') as data_file:
        data = json.load(data_file)

    data['orders'].append(order)
    with open('orders.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


write_order_to_json('ноутбук', 1, 210000, 'Сергей', '22.11.2018')
write_order_to_json('монитор', 3, 57900, 'Егор', '21.11.2018')

