import random
import sys

############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк" 

################## Шифр А5/1 ##################
print("\n################## Шифр А5/1 ##################\n")

# Обнуляем списки значений регистров
reg1 = [0] * 19
reg2 = [0] * 22
reg3 = [0] * 23

list_old_alphabet = [] # Составляем список для алфавита формата ['a', 'б', ...]
for i in old_alphabet:
    list_old_alphabet.append(i)
list_full_alphabet = [] # То же самое для расширенного алфавита
for i in full_alphabet:
    list_full_alphabet.append(i)

def key_generator():
    key = [0] * 64 # Определяем размер ключа
    for i in range(0, 64): # Генерируем рандомный ключ
        key[i] = random.randint(0, 1)
    return key

def to_binary(message, abc):
    msgbits = []
    numeric = [abc.index(i) + 1 for i in list(message)] # Составляем список индексов символов текста в алфавите
    for i in numeric: 
        x = format(i, 'b') # Переводим сообщение в двоичный код
        if len(x) < 11: # Eсли двоичное представление числа меньше 11 бит, 
            x = '0' * (11 - len(x)) + x # то добавляем в начало нули
        elif len(x) > 11:
            sys.exit()
        for j in x:
            msgbits.append(int(j))
    return msgbits

def from_binary(bits, abc):
    res = []
    for i in range(len(''.join(map(str, bits))) // 11): # Переводим сообщение в символьный вид
        res.append(int(''.join(map(str, bits))[i*11:i*11+11], 2))
    text = []
    for i in res: # Переводим символы-индексы обратно в текстовые символы
        if (int(i) - 1) <= len(abc):
            text.append(abc[i - 1])
    return ''.join(map(str, text))

def clock():
    global reg1, reg2, reg3
    # Вычисляем функцию большинства majority
    majority = ((reg1[8] & reg2[10]) | (reg1[8] & reg3[10]) | (reg2[10] & reg3[10]))
    if reg1[8] == majority: # Проверяем контрольные биты синхронизации
        clockone() # В случае совпадения значений контрольных битов со значением функции
    if reg2[10] == majority:
        clocktwo()
    if reg3[10] == majority:
        clockthree()

# Набор функций, реализующих сдвиги регистров
def clockone(): # Для регистра R1
    global reg1
    temp = 0
    # Функции обратной связи задаются разными полиномами для R1, R2 и R3
    temp = reg1[13] ^ reg1[16] ^ reg1[17] ^ reg1[18]
    for i in reversed(range(len(reg1))):
        reg1[i] = reg1[i - 1] # Результат становится новым значением крайнего правого бита
        if i == 1:
            reg1[0] = temp

def clocktwo(): # Аналогично функции clockone(), но для R2
    global reg2
    temp = 0
    temp = reg2[20] ^ reg2[21]
    for i in reversed(range(len(reg2))):          
        reg2[i] = reg2[i - 1]
        if i == 1:
            reg2[0] = temp

def clockthree(): # Аналогично функции clockone(), но для R3
    global reg3
    temp = 0
    temp = reg3[7] ^ reg3[20] ^ reg3[21] ^ reg3[22]
    for i in reversed(range(len(reg3))):
        reg3[i] = reg3[i - 1]
        if i == 1:
            reg3[0] = temp


def reg_states(key, frame_temp): # Заполняем списки значений состояний регистров
    global reg1, reg2, reg3
    # Обнуляем списки значений регистров
    reg1 = [0] * 19
    reg2 = [0] * 22
    reg3 = [0] * 23

    for i in range(0, 64): # 64 такта, операция XOR производится с битом ключа
        clockone()
        clocktwo()
        clockthree()
        reg1[0] = reg1[0] ^ key[i]
        reg2[0] = reg2[0] ^ key[i]
        reg3[0] = reg3[0] ^ key[i]
    
    frame = [int(item) for item in list(format(frame_temp, 'b'))]
    while len(frame) != 22:
        frame.insert(0, 0)

    for i in range(0, 22): # 22 такта, операция XOR производится с номером кадра
        clockone()
        clocktwo()
        clockthree()
        reg1[0] = reg1[0] ^ frame[i]
        reg2[0] = reg2[0] ^ frame[i]
        reg3[0] = reg3[0] ^ frame[i]

    for i in range(0, 100): # 100 тактов с управлением сдвигами регистров, 
        clock() # но без генерации последовательности
    
    return get_keystream(114)

def get_keystream(length=114): # 114 тактов
    global reg1, reg2, reg3
    keystream = []
    for i in range(length):
        clock()
        # Для получения выходного бита системы XOR над выходными битами регистров
        keystream.append(reg1[18] ^ reg2[21] ^ reg3[22])
    return keystream


def A5_1(message, abc, key):
    msgbits = to_binary(message, abc)
    keystream_full = [] # Переменная для сохранения всего ключевого потока
    encrypted_bits = []
    decrypted_bits = []
    # Передача данных осуществляется с разбивкой на кадры по 114 бит
    framescount = len(msgbits) // 114 
    if ((len(msgbits) % 114) != 0):
        framescount += 1
    frame = 0 # Для каждого кадра
    for i in range(framescount): # Шифрование
        keystream = reg_states(key, frame) # Инициализируем регистры R1, R2, R3
        if i == 0:
            print('R1: ', ''.join(map(str, reg1)))
            print('R2: ', ''.join(map(str, reg2)))
            print('R3: ', ''.join(map(str, reg3)))
        [keystream_full.append(i) for i in keystream]
        frame += 1
        for j in range(0, 114):
            if (i * 114 + j) >= len(msgbits): # Если выходим за границы длины сообщения
                break
            encrypted_bits.append(msgbits[i * 114 + j] ^ keystream[j])
            
    frame = 0    
    for i in range(framescount): # Расшифрование
        keystream = reg_states(key, frame)
        frame += 1
        for j in range(0, 114):
            if (i * 114 + j) >= len(msgbits): # Если выходим за границы длины сообщения
                break
            decrypted_bits.append(encrypted_bits[i * 114 + j] ^ keystream[j])

    text = from_binary(decrypted_bits, abc)

    return ''.join(map(str, msgbits)), ''.join(map(str, keystream_full)), ''.join(map(str, encrypted_bits)), ''.join(map(str, decrypted_bits)), ''.join(text)


print("Часть поговорки: " + pogovorka[:2]) # Проверяем на части поговорки
key = [int(item) for item in list('0011101001100110101011001011010100101011000110110000011011000001')]
print("Ключ: ", ''.join(map(str, key)))
encrypted = A5_1(pogovorka[:2], list_old_alphabet, key)
print("Часть поговорки в двоичном виде: ", encrypted[0])
print("Ключевой поток: ", encrypted[1][:22])
print("Зашифрованная часть поговорки в двоичном виде: ", encrypted[2], "\nРасшифрованная часть поговорки в двоичном виде: ", encrypted[3])
print("Расшифрованная часть поговорки: ", encrypted[4])

print("Поговорка: " + pogovorka) # Проверяем на поговорке
key = [int(item) for item in list('0011101001100110101011001011010100101011000110110000011011000001')]
print("Ключ: ", ''.join(map(str, key)))
encrypted = A5_1(pogovorka, list_old_alphabet, key)
print("Поговорка в двоичном виде: ", encrypted[0])
print("Ключевой поток: ", encrypted[1])
print("Зашифрованная поговорка в двоичном виде: ", encrypted[2], "\nРасшифрованная поговорка в двоичном виде: ", encrypted[3])
print("Расшифрованная поговорка: ", encrypted[4])

str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
key = key_generator() # Генерируем ключ
print("Ключ: ", ''.join(map(str, key)))
encrypted1 = A5_1(str1, list_full_alphabet, key)
print("Cообщение в двоичном виде: ", encrypted1[0])
print("Ключевой поток: ", encrypted[1])
print("Зашифрованное сообщение в двоичном виде: ", encrypted1[2], "\nРасшифрованное сообщение в двоичном виде: ", encrypted1[3])
print("Расшифрованное сообщение: ", encrypted1[4])
input("Нажмите Enter, чтобы закрыть программу.")