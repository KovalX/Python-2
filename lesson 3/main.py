import time
from subprocess import Popen, CREATE_NEW_CONSOLE

process_list = []

while True:
    user = input('Запустить сервер и клиентов (s) / Выйти (q)')

    if user == 's':
        process_list.append(Popen('python server.py', creationflags=CREATE_NEW_CONSOLE))
        print('Сервер запущен')
        time.sleep(2)

        for _ in range(3):
            process_list.append(Popen('python -i client.py localhost 7777 r', creationflags=CREATE_NEW_CONSOLE))
        print('Клиенты для чтения запущены')

        for _ in range(2):
            process_list.append(Popen('python -i client.py localhost 7777 w', creationflags=CREATE_NEW_CONSOLE))
        print('Клиенты на запись запущены')

    elif user == 'q':
        print("Открыто процессов {}".format(len(process_list)))
        for process in process_list:
            print("Закрываю процесс {}".format(process))
            process.kill()
        process_list.clear()
        print("Выход")
        break

