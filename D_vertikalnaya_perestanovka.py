import numpy as np 

############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк" 

################## ВЕРТИКАЛЬНАЯ перестановка ##################
print("\n################## ВЕРТИКАЛЬНАЯ перестановка ##################\n")

old_key = 'ювелирный'

def order(key):
    for i, ch in zip(range(len(key)), sorted(list(key))): # Нумеруем сортированный по алфавиту список символов
        key = key.replace(ch, str(i)) # Заменяем символ его номером
    return [int(i) for i in key]

def vertikalnaya_perestanovka(message, key, abc, en_or_de):
    if abc == 1:
        abc_tmp = old_alphabet
    if abc == 2:
        abc_tmp = full_alphabet
    abc_internal = []
    for i in abc_tmp:
        abc_internal.append(abc_tmp.index(i) + 1)
    abc_internal.append('null')
    message_list = []
    encrypted_message = []
    if en_or_de == "en":
        for i in message:
            message_list.append(abc_tmp.index(i) + 1)
        shape = (((len(message_list) // len(key)) + 1), len(key)) # Определяем размерность таблицы
        # Дополняем текст пустыми символами для создания таблицы с требуемым числом столбцов
        for i in range((((len(message_list) // len(key)) + 1) * len(key)) - len(message_list)):
            message_list.append(abc_internal[-1])
        # Создаем таблицу в виде матрицы и транспонируем для простоты обращения к столбцам
        table = np.matrix(message_list).reshape(shape).T
        for i in order(key): # Расставляем символы ключа в алфавитном порядке
            encrypted_message.append(table[i].tolist()[0]) # Берем из таблицы символы в правильном порядке
    if en_or_de == "de":
        for i in message: # Переводим вложенный список в обычный, чтобы сделать правильную таблицу
            for j in i:
                message_list.append(j)
        shape = (len(key), (len(message_list) // len(key))) # Определяем размерность таблицы
        table = np.matrix(message_list).reshape(shape) # Строим таблицу
        key_list = order(key) # Определяем порядок символов по алфавиту в ключе
        for i in range(len(key)):
            j = key_list.index(i)
            encrypted_message.append(table[j].tolist()[0]) # И перемещаем столбцы
    return encrypted_message

# Преобразуем матрицу с переставленными столбцами в исходное положение и убираем пустой символ
def clear(message, abc, en_or_de, key):
    clean_message = []
    if en_or_de == 'en':
        for i in message:
            for j in i:
                if j != 'null':
                    if abc == 1:
                        clean_message.append(old_alphabet[int(j) - 1]) 
                    else:
                        clean_message.append(full_alphabet[int(j) - 1])
    if en_or_de == 'de':
        for i in range(sum([len(element) for element in message]) // len(key)):
            for j in range(len(message)):
                if message[j][i] != 'null':
                    if abc == 1:
                        clean_message.append(old_alphabet[int(message[j][i]) - 1]) 
                    else:
                        clean_message.append(full_alphabet[int(message[j][i]) - 1]) 
        
    return ''.join(clean_message)

print("Поговорка: " + pogovorka) # Проверяем на поговорке
print("Ключ: ", old_key)
encrypted = vertikalnaya_perestanovka(pogovorka, old_key, 1, "en")
decrypted = vertikalnaya_perestanovka(encrypted, old_key, 1, "de")
print("Зашифрованное сообщение: " + str(clear(encrypted, 1, 'en', old_key)) + "\n" + "Расшифрованное сообщение: " + str(clear(decrypted, 1, 'de', old_key)))

str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
str2 = input("Введите ключ: ")
# Проверка ключа
okay = 0
while okay == 0:
    if len(str2) != len(set(str2)):
        print('Ключ должен содержать только уникальные символы. Попробуйте еще раз.')
        str2 = input("Введите ключ: ")
    else:
        okay = 1
encrypted = vertikalnaya_perestanovka(str1, str2, 2, "en")
decrypted = vertikalnaya_perestanovka(encrypted, str2, 2, "de")
print("Зашифрованное сообщение: " + str(clear(encrypted, 2, 'en', str2)) + "\n" + "Расшифрованное сообщение: " + str(clear(decrypted, 2, 'de', str2)))
input("Нажмите Enter, чтобы закрыть программу.")
