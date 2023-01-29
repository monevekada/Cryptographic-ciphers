import numpy as np 
import numpy.linalg as linalg

############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк"

################## МАТРИЧНЫЙ шифр ##################
print("\n################## МАТРИЧНЫЙ шифр ##################\n")

# Сгенерируем псевдослучайный ключ выбранного порядка
def key_generator(number):
    key = np.matrix(np.random.randint(number, size=(number,number)))
    return key

old_key = np.array([[1, 4, 8], [3, 7, 2], [6, 9, 5]])

void_count = 0 # Создаем переменную для хранения количества пустых символов в последнем векторе

# Функция для заполнения последнего блока пустыми символами
def separate(text, block_size, abc):
    vectors = []
    if abc == 1:
        if len(text) % block_size: # Если недостает символов для заполнения последнего блока
            void_count = block_size - (len(text) % block_size) # Находим количество пустых символов
            text = text + [0] * void_count
    else:
        if len(text) % block_size: 
            void_count = block_size - (len(text) % block_size) 
            text = text + [0] * void_count
            
    for i in range(0, len(text), block_size):
        block = text[i:i+block_size] # Разбиваем числовой эквивалент на векторы заданной длины
        vectors.append(block) # Помещаем все векторы в один список для удобства
    return vectors

# Шифрование и расшифрование
def matrix(message, key, abc, en_or_de):
    if en_or_de == "en":            
        if abc == 1: # Выбираем алфавит
            encrypted_message = [] # Создаем переменную для хранения результатов умножения матрицы на векторы
            T = [] # Определяем числовой эквивалент Tэ открытого текста
            for i in message: # Для каждого символа открытого текста находим его номер в алфавите
                T.append(old_alphabet.index(i) + 1) 
            # Разбиваем Tэ на векторы B, длина которых соответствует порядку ключа-матрицы
            B = separate(T, np.size(key, 0), 1)
            for block in B: # Умножаем матрицу на каждый вектор
                vector = key * np.matrix(block).swapaxes(0,1)
                # И прибавляем к зашифрованному сообщению в конец числа при каждом умножении
                encrypted_message.extend(vector.squeeze().tolist()[0])
            encrypted_message = ' '.join([str(i) for i in encrypted_message])
        else:
            encrypted_message = [] # Создаем переменную для хранения результатов умножения матрицы на векторы
            T = [] # Определяем числовой эквивалент Tэ открытого текста
            for i in message: # Для каждого символа открытого текста находим его номер в алфавите
                T.append(full_alphabet.index(i) + 1) 
            # Разбиваем Tэ на векторы B, длина которых соответствует порядку ключа-матрицы
            B = separate(T, np.size(key, 0), 1)
            for block in B: # Умножаем матрицу на каждый вектор
                vector = key * np.matrix(block).swapaxes(0,1)
                # И прибавляем к зашифрованному сообщению в конец числа при каждом умножении
                encrypted_message.extend(vector.squeeze().tolist()[0])
            encrypted_message = ' '.join([str(i) for i in encrypted_message])
    if en_or_de == "de":
        if abc == 1:
            encrypted_message = []
            for block in separate(message.split(), np.size(key, 0), 1):
                vector = np.matrix([int(i) for i in block]).swapaxes(0,1)
                res = linalg.inv(key) * vector # Умножаем обратную матрицу на вектор шифртекста
                res = np.matrix.round(res,0).astype(int) # Приводим результат к целому типу
                res = res.squeeze().tolist()[0]
                # По индексу символа в алфавите восстановим блок исходного сообщения
                for i in res: # Для начала удалим пустые символы с конца
                    if i != 0:
                        encrypted_message.extend(old_alphabet[i-1])   
            encrypted_message = encrypted_message[:len(encrypted_message)]   
        else:
            encrypted_message = []
            for block in separate(message.split(), np.size(key, 0), 1):
                vector = np.matrix([int(i) for i in block]).swapaxes(0,1)
                res = linalg.inv(key) * vector # Умножаем обратную матрицу на вектор шифртекста
                res = np.matrix.round(res,0).astype(int) # Приводим результат к целому типу
                res = res.squeeze().tolist()[0]
                # По индексу символа в алфавите восстановим блок исходного сообщения
                for i in res: # Для начала удалим пустые символы с конца
                    if i != 0:
                        encrypted_message.extend(full_alphabet[i-1])   
            encrypted_message = encrypted_message[:len(encrypted_message)]
    return encrypted_message

print("Поговорка: " + pogovorka) # Проверяем на поговорке
print("Ключ: ", old_key)
encrypted = matrix(pogovorka, old_key, 1, "en")
decrypted = matrix(encrypted, old_key, 1, "de")
print("Зашифрованное сообщение: " + ''.join(map(str, encrypted)) + "\n" + "Расшифрованное сообщение: " + ''.join(map(str, decrypted)))


str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
str2 = input("Введите порядок ключа-матрицы: ")
# Проверка ключа
okay = 0
while okay == 0:
    # Проверяем, введено ли число, а также задаем границы порядка матрицы от 3 до длины текста
    if not str2.isnumeric() or int(str2) > len(str1) or int(str2) < 3:
        print("Порядок должен быть целым числом от 3. Попробуйте еще раз.")
        str2 = input("Введите ключ: ")
    else:
        okay = 1
str_key = key_generator(int(str2))
encrypted = matrix(str1, str_key, 2, "en")
decrypted = matrix(encrypted, str_key, 2, "de")
print("Зашифрованное сообщение: " + ''.join(map(str, encrypted)) + "\n" + "Расшифрованное сообщение: " + ''.join(map(str, decrypted)))
input("Нажмите Enter, чтобы закрыть программу.")
