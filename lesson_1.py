import subprocess
import locale

# Task 1
word_1 = 'разработка'
word_2 = 'сокет'
word_3 = 'декоратор'
print(word_1, word_2, word_3)
print(type(word_1), type(word_2), type(word_3))

uni_word_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(uni_word_1, type(uni_word_1))

uni_word_2 = '\u0441\u043e\u043a\u0435\u0442'
print(uni_word_2, type(uni_word_2))

uni_word_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(uni_word_3, type(uni_word_3))


# Task 2
# word_b1 = b'class'
# word_b2 = b'function'
# word_b3 = b'method'
#
# print(word_b1, type(word_b1), len(word_b1))
# print(word_b2, type(word_b2), len(word_b2))
# print(word_b3, type(word_b3), len(word_b3))

# Task 3
#  bytes can only contain ASCII literal characters
# st_1 = b'attribute'
# st_2 = b'класс'
# st_3 = b'функция'
# st_4 = b'type'

# Task 4
# word1 = 'разработка'
# word2 = 'администрирование'
# word3 = 'protocol'
# word4 = 'standard'
#
# new_word1 = word1.encode('utf-8')
# print(new_word1)
# dec_word1 = new_word1.decode('utf-8')
# print(dec_word1)
#
# new_word2 = word2.encode('utf-8')
# print(new_word2)
# dec_word2 = new_word2.decode('utf-8')
# print(dec_word2)
#
# new_word3 = word3.encode('utf-8')
# print(new_word3)
# dec_word3 = new_word3.decode('utf-8')
# print(dec_word3)
#
# new_word4 = word4.encode('utf-8')
# print(new_word4)
# dec_word4 = new_word4.decode('utf-8')
# print(dec_word4)

# Task 5
# args = ['ping', 'yandex.ru']
# sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in sub_ping.stdout:
#     print(line.decode('cp866'))
#
#
# args_1 = ['ping', 'youtube.com']
# sub_ping_proc = subprocess.Popen(args_1, stdout=subprocess.PIPE)
# for line in sub_ping_proc.stdout:
#     line = line.decode('cp866').encode('utf-8')
#     print(line.decode('utf-8'))


# Task 6
# with open('test_file.txt', 'w', encoding='utf-8') as file:
#     file.write('сетевое программирование\n')
#     file.write('сокет\n')
#     file.write('декоратор')
#
#
# def_coding = locale.getpreferredencoding()
# print(def_coding)
#
# with open('test_file.txt', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')

