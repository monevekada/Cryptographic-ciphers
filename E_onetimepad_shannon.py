import random
import sys

############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк" 

################## Одноразовый блокнот ШЕННОНА ##################
print("\n################## Одноразовый блокнот ШЕННОНА ##################\n")

def key_generator(message_len, abc):
    key = []
    for i in range(message_len):
        if abc == 1:
            key.append(random.randint(0, len(old_alphabet)))
        elif abc == 2:
            key.append(random.randint(0, len(full_alphabet)))
    return key

def onetimepad(message, key, abc, en_or_de):
    if abc == 1:
        list_alphabet = [] # Составляем список для алфавита формата ['a', 'б', ...]
        for i in old_alphabet:
            list_alphabet.append(i)
        dist_alphabet = {} # Составляем словарь для алфавита формата {'a':'0', 'б':'1', ...}
        for i in list_alphabet:
            dist_alphabet[i] = list_alphabet.index(i)
    if abc == 2:
        list_alphabet = [] # То же самое для расширенного алфавита
        for i in full_alphabet:
            list_alphabet.append(i)
        dist_alphabet = {}
        for i in list_alphabet:
            dist_alphabet[i] = list_alphabet.index(i)
    n = int(len(list_alphabet)) # Находим длину выбранного алфавита
    encrypted_message_tmp = []
    encrypted_message = ''
    message_list = []
    if en_or_de == 'en':
        for i in message: # Переводим символы сообщения в формат чисел
            message_list.append(list_alphabet.index(i) + 1)
        for i, j in zip(message_list, key): # Непосредственно шифруем, mod (длина алфавита)
            encrypted_message_tmp.append((i + j) % n)
        for i in encrypted_message_tmp:
            encrypted_message += list_alphabet[i]
    if en_or_de == 'de':
        for i in message:
            message_list.append(list_alphabet.index(i))
        for i, j in zip(message_list, key):
            if i > j: 
                encrypted_message_tmp.append(i - j)
            else: # Если символ сообщения меньше соответствующего символа ключа, добавим длину сообщения
                encrypted_message_tmp.append(i + n - j) 
        for i in encrypted_message_tmp:
            encrypted_message += list_alphabet[i - 1]
    return encrypted_message


print("Поговорка: " + pogovorka) # Проверяем на поговорке
key = [28, 26, 27, 19, 26, 30, 10, 28, 1, 15, 18, 13, 23, 9, 4, 12, 15, 20, 32, 32, 26, 2, 31, 17,
    15, 24, 32, 32, 21, 22, 5, 23, 26, 24, 28, 21, 30, 20, 19, 10, 17, 8, 28, 2, 2, 5, 22, 14, 7, 25, 14, 10]
key_tmp = ''
for i in key:
    key_tmp += old_alphabet[int(i) - 1]
print("Ключ: ", key_tmp)
encrypted = onetimepad(pogovorka, key, 1, "en")
decrypted = onetimepad(encrypted, key, 1, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)

str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
key = []
key = key_generator(len(str1), 2)
key_tmp = ''
for i in key:
    key_tmp += full_alphabet[int(i) - 1]
print("Ключ: ", key_tmp)
encrypted = onetimepad(str1, key, 2, "en")
decrypted = onetimepad(encrypted, key, 2, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)
input("Нажмите Enter, чтобы закрыть программу.")
