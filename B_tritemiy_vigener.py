############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк"

################## Шифр ТРИТЕМИЯ ##################
print("\n################## Шифр ТРИТЕМИЯ ##################\n")

# Шифрование и расшифрование
def trithemius(message, abc, en_or_de):
    list_old_alphabet = [] # Составляем список для алфавита формата ['a', 'б', ...]
    for i in old_alphabet:
        list_old_alphabet.append(i)
    dist_old_alphabet = {} # Составляем словарь для алфавита формата {'a':'0', 'б':'1', ...}
    for i in list_old_alphabet:
        dist_old_alphabet[i] = list_old_alphabet.index(i)

    list_full_alphabet = [] # То же самое для расширенного алфавита
    for i in full_alphabet:
        list_full_alphabet.append(i)
    dist_full_alphabet = {}
    for i in list_full_alphabet:
        dist_full_alphabet[i] = list_full_alphabet.index(i)

    old_key = old_alphabet[1:] + old_alphabet[0] # Ключ принимает вид: бвгдеёжзийклмнопрстуфхцчшщьыъэюяа,
    full_key = full_alphabet[1:] + full_alphabet[0] # т.е. первый символ алфавита перемещается в его конец

    if en_or_de == "en":
        if abc == 1: # Выбираем алфавит
            encrypted_message = message[0] # Присваиваем первый символ открытого текста зашифрованному
            for i in message[1:]: # Для каждого последующего символа открытого текста
                # Прибавляем зашифрованному сообщению символ ключа под следующим номером символа алфавита
                encrypted_message += old_key[int(dist_old_alphabet[i])] 
                old_key = old_key[1:] + old_key[0] # Первый символ ключа перемещается в его конец
        else:
            encrypted_message = message[0] 
            for i in message[1:]: 
                encrypted_message += full_key[int(dist_full_alphabet[i])] 
                full_key = full_key[1:] + full_key[0] 
    if en_or_de == "de":
        if abc == 1:
            encrypted_message = message[0]
            for i in message[1:]:
                # Прибавляем расшифрованному сообщению символ алфавита под следующим номером символа ключа
                encrypted_message += old_alphabet[int(old_key.find(i))]
                old_key = old_key[1:] + old_key[0] # Первый символ ключа перемещается в его конец
        else:
            encrypted_message = message[0]
            for i in message[1:]:
                encrypted_message += full_alphabet[int(full_key.find(i))]
                full_key = full_key[1:] + full_key[0]          
    return encrypted_message


print("Поговорка: " + pogovorka) # Проверяем на поговорке
encrypted = trithemius(pogovorka, 1, "en")
decrypted = trithemius(encrypted, 1, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
encrypted = trithemius(str1, 2, "en")
decrypted = trithemius(encrypted, 2, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


################## Шифр ВИЖЕНЕРА ##################
print("\n################## Шифр ВИЖЕНЕРА ##################\n")

old_key_vigener = 'ъ' + pogovorka[:-1] # Старый ключ для проверки работоспособности программы с поговоркой

# Шифрование и расшифрование
def vigener(message, key, abc, en_or_de):
    old_tritemiy_table = [] # Построим таблицу Тритемия для старого алфавита
    row = old_alphabet
    for i in old_alphabet:
        list_in_table = list(row)
        old_tritemiy_table.append(list_in_table)
        row = row[1:] + row[:1]

    list_in_table = [] # Обнуляем переменную, чтобы алфавиты не смешались
    full_tritemiy_table = []
    row = full_alphabet
    for i in full_alphabet:
        list_in_table = list(row)
        full_tritemiy_table.append(list_in_table)
        row = row[1:] + row[:1]

    row_num = 0 # Введем переменные номеров столбца и строки
    col_num = 0
    shift = 0 # Введем переменную для смещения индекса элемента ключа

    if en_or_de == "en":
        if abc == 1: # Выбираем алфавит
            encrypted_message = ''
            for i in message: # Для каждого последующего элемента открытого текста
                # Находим номер столбца таблицы Тритемия по символу открытого текста
                col_num = old_tritemiy_table[0].index(i) 
                k = 0
                for j in old_tritemiy_table: # Находим номер строки таблицы Тритемия по символу ключа
                    if old_tritemiy_table[k][0] == key[shift]:
                        row_num = k
                    k = k + 1
                encrypted_message = encrypted_message + old_tritemiy_table[row_num][col_num]
                shift = shift + 1
            shift = 0 # Обнуляем переменную сдвига по ключу
        else:
            key = key + message[:-1]
            encrypted_message = ''
            for i in message: 
                col_num = full_tritemiy_table[0].index(i) 
                k = 0
                for j in full_tritemiy_table: 
                    if full_tritemiy_table[k][0] == key[shift]:
                        row_num = k
                    k = k + 1
                encrypted_message = encrypted_message + full_tritemiy_table[row_num][col_num]
                shift = shift + 1
            shift = 0 # Обнуляем переменную сдвига по ключу
    if en_or_de == "de":
        if abc == 1:
            encrypted_message = ''
            for i in message: # Для каждого последующего элемента зашифрованного текста
                k = 0
                for j in old_tritemiy_table: # Находим номер строки таблицы Тритемия по символу ключа
                    if old_tritemiy_table[k][0] == key[shift]:
                        row_num = k
                    k = k + 1
                # Находим номер столбца таблицы Тритемия по символу зашифрованного текста
                col_num = old_tritemiy_table[row_num].index(i) 
                k = 0
                # Прибавляем к расшифрованному сообщению символ первой строки таблицы с найденным индексом
                encrypted_message = encrypted_message + old_tritemiy_table[0][col_num]
                key = key + old_tritemiy_table[0][col_num] # Добавляем к ключу расшифрованный символ
                shift = shift + 1
            shift = 0 # Обнуляем переменную сдвига по ключу
        else:
            encrypted_message = ''
            for i in message:
                k = 0
                for j in full_tritemiy_table:
                    if full_tritemiy_table[k][0] == key[shift]:
                        row_num = k
                    k = k + 1
                col_num = full_tritemiy_table[row_num].index(i) 
                k = 0
                encrypted_message = encrypted_message + full_tritemiy_table[0][col_num]
                key = key + full_tritemiy_table[0][col_num] 
                shift = shift + 1
            shift = 0 # Обнуляем переменную сдвига по ключу

    return encrypted_message


print("Поговорка: " + pogovorka) # Проверяем на поговорке
print("Ключ: ", old_key_vigener)
encrypted = vigener(pogovorka, old_key_vigener, 1, "en")
decrypted = vigener(encrypted, old_key_vigener, 1, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
str2 = input("Введите ключ: ")
# Проверка ключа
if len(str2) > 1: 
    print("Ключ должен содержать один символ. Попробуйте еще раз.")
    str2 = input("Введите ключ: ")
if str2 not in full_alphabet:
    print("Ключ должен быть символом, который содержится в алфавите. Попробуйте еще раз.")
    str2 = input("Введите ключ: ")
encrypted = vigener(str1, str2, 2, "en")
decrypted = vigener(encrypted, str2, 2, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)
input("Нажмите Enter, чтобы закрыть программу.")
