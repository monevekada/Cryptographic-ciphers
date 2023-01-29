############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк"

################## Шифр АТБАШ ##################
print("\n################## Шифр АТБАШ ##################\n")

# Шифрование и расшифрование
def atbash(message, abc, en_or_de):
    if abc == 1:
        alphabet = old_alphabet
        reversed_alphabet = old_alphabet[::-1] # Переворачиваем алфавит
    else:
        alphabet = full_alphabet
        reversed_alphabet = full_alphabet[::-1]
    encrypted_message = ""
    for letter in message:
        if letter in alphabet:
            if en_or_de == "en": # Если выбрано "Шифрование"
                new_letter = reversed_alphabet[alphabet.index(letter)] # Получаем новый символ
            else: # Если выбрано "Расшифрование"
                new_letter = alphabet[reversed_alphabet.index(letter)]
            encrypted_message += new_letter
        else: # Если символ в алфавите не найден, переписываем его без изменения
            encrypted_message += letter
    return encrypted_message 


print("Поговорка: " + pogovorka) # Проверяем на поговорке
encrypted = atbash(pogovorka, 1, "en")
decrypted = atbash(encrypted, 1, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
encrypted = atbash(str1, 2, "en")
decrypted = atbash(encrypted, 2, "de")
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


########## Шифр Цезаря (произвольный) ##########
print("\n########## Шифр Цезаря (произвольный) ##########\n")

# Шифрование
def caesar_encryption(message, abc, shift):
    encrypted_message = ""
    for letter in message:
        if abc == 1: # Выбираем алфавит
            if letter in old_alphabet:
                index = old_alphabet.index(letter) # Ищем нужный символ в алфавите
                n = index + shift # Прибавляем к индексу символа сдвиг
                if n >= len(old_alphabet): # Если индекс символа больше, чем всего символов в алфавите, то
                    n = n - len(old_alphabet) # начинаем отсчет с начала алфавита
                encrypted_message += old_alphabet[n]
            else: # Если символ в алфавите не найден, переписываем его без изменения
                encrypted_message += letter
        elif abc == 2:
            if letter in full_alphabet:
                index = full_alphabet.index(letter)
                n = index + shift
                if n >= len(full_alphabet):
                    n = n - len(full_alphabet)
                encrypted_message += full_alphabet[n]
            else: 
                encrypted_message += letter
    return encrypted_message

# Расшифрование
def caesar_decryption(message, abc, shift):
    decrypted_message = ""
    for letter in message:
        if abc == 1:
            if letter in old_alphabet:
                index = old_alphabet.index(letter)
                n = index - shift # От шифрования расшифрование отличается вычитанием сдвига
                decrypted_message += old_alphabet[n]
            else:
                decrypted_message += letter
        elif abc == 2:
            if letter in full_alphabet:
                index = full_alphabet.index(letter)
                n = index - shift
                decrypted_message += full_alphabet[n]
            else:
                decrypted_message += letter
    return decrypted_message

shift = input("Введите ключ: ")
# Проверка ключа
okay = 0
while okay == 0:
    # Проверяем, введено ли число, большее 1 и меньшее значения длины используемого алфавита
    if not shift.isnumeric() or int(shift) >= len(old_alphabet) or int(shift) < 1:
        print("Ключ должен быть целым числом от 1 и до значения длины используемого алфавита. Попробуйте еще раз.")
        shift = input("Введите ключ: ")
    else:
        okay = 1
shift = int(shift)
print("Поговорка: " + pogovorka) # Проверяем на поговорке
encrypted = caesar_encryption(pogovorka, 1, shift)
decrypted = caesar_decryption(encrypted, 1, shift)
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
encrypted = caesar_encryption(str1, 2, shift)
decrypted = caesar_decryption(encrypted, 2, shift)
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


################# Шифр Полибия #################

print("\n########## Шифр Полибия ##########\n")

matrix_old_alphabet = [['а','б','в','г','д','е'],
         ['ж','з','и','й','к','л'],
         ['м','н','о','п','р','с'],
         ['т','у','ф','х','ц','ч'],
         ['ш','щ','ъ','ы','ь','э'],
         ['ю','я','-','-','-','-']]

matrix_old_height = len(matrix_old_alphabet) # Находим длину матрицы алфавита (внешнюю)
matrix_old_width = len(matrix_old_alphabet[0]) # Находим ширину матрицы алфавита (длину внутренней)

matrix_full_alphabet = [['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','!','\"',' ','…'],
         ['#','$','%','&','\'','(',')','*','+','-','—','«','»','.',',','<','>','?','/','|','\\',';',':','№','_','=','[',']','{','}','`','~','1','2','3','4','5','6','7','8','9','0','А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё'],
         ['Ж','ж','З','з','И','и','Й','й','К','к','Л','л','М','м','Н','н','О','о','П','п','Р','р','С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш','Щ','щ','Ь','ь','Ы','ы','Ъ','ъ','Э','э','Ю','ю','Я','я','€','ˈ','“','”']]

matrix_full_height = len(matrix_full_alphabet) 
matrix_full_width = len(matrix_full_alphabet[0])
 
 
# Шифрование
def polibiy_encryption(message, alphabet):
    encrypted_message = ""
    for index in range(0, len(message)): # Рассматриваем по одному символу из текста
        if alphabet == 1:
            encrypted_message += get_a_number(message[index], 1) # Добавляем каждый новый зашифрованный символ к зашифрованному тексту
        if alphabet == 2: 
            encrypted_message += get_a_number(message[index], 2)
    return encrypted_message

def get_a_number(letter, alphabet):
    i = ''
    j = ''
    if alphabet == 1:
        for index_old_height in range(0, matrix_old_height):
            for index_old_width in range(0, matrix_old_width):
                if letter == matrix_old_alphabet[index_old_height][index_old_width]: # Если нашли символ:
                    i = str(index_old_height + 1)
                    j = str(index_old_width + 1)
                    return i+j # Записываем его координаты
    if alphabet == 2:
        for index_full_height in range(0, matrix_full_height):
            for index_full_width in range(0, matrix_full_width):
                if letter == matrix_full_alphabet[index_full_height][index_full_width]:
                    if index_full_height < 10: # Делаем числа строками
                        i = '0' + str(index_full_height)
                    else:
                        i = str(index_full_height)
                    if index_full_width < 10:
                        j = '0' + str(index_full_width)
                    else:
                        j = str(index_full_width)
                    return i + j
    return letter # Если не нашли символ в алфавите
 
# Расшифрование
def polibiy_decryption(message, alphabet):
    decrypted_message = ""
    if alphabet == 1:
        for index in range(0, len(message), 2):
            index = str(message[index : index + 2])
            decrypted_message += get_a_letter(index, 1)
    else:
        for index in range(0, len(message), 4):
            #if index == ' ':
                #decrypted_message += ' '
            #else:
            index = str(message[index : index + 4])
            decrypted_message += get_a_letter(index, 2)
    return decrypted_message

def get_a_letter(number, alphabet):
    if alphabet == 1:
        if number:
            index_old_height = number[0]
            index_old_width = number[1]
            if matrix_old_alphabet[int(index_old_height) - 1][int(index_old_width) - 1]: # Если нашли символ по координатам:
                return matrix_old_alphabet[int(index_old_height) - 1][int(index_old_width) - 1] # Записываем его
    if alphabet == 2:
        i = 0
        j = 0
        if number:
            index_full_height = number[0] + number[1]
            if index_full_height[0] == '0': # Удаляем лишние нули для нормального считывания индексов
                index_full_height = number[1]
            index_full_width = number[2] + number[3]
            if index_full_width[0] == '0':
                index_full_width = number[3]
            i = int(index_full_height)
            j = int(index_full_width)
            if matrix_full_alphabet[i][j]: # Если нашли символ по координатам:
                return matrix_full_alphabet[i][j]
    return number # Если не нашли символ в алфавите
 

print("Поговорка: " + pogovorka) # Проверяем на поговорке
encrypted = polibiy_encryption(pogovorka, 1)
decrypted = polibiy_decryption(encrypted, 1)
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)


str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
encrypted = polibiy_encryption(str1, 2)
decrypted = polibiy_decryption(encrypted, 2)
print("Зашифрованное сообщение: " + encrypted + "\n" + "Расшифрованное сообщение: " + decrypted)
input("Нажмите Enter, чтобы закрыть программу.")
