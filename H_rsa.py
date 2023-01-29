############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz#$%&€ˈ“”…\'*+<>?/|\\;:№_=[]{}`~\"1234567890.,!«»-— АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя()"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк" 

################## RSA ##################
print("\n################## RSA ##################\n")

list_old_alphabet = [] # Составляем список для алфавита формата ['a', 'б', ...]
for i in old_alphabet:
    list_old_alphabet.append(i)
list_full_alphabet = [] # То же самое для расширенного алфавита
for i in full_alphabet:
    list_full_alphabet.append(i)

def evklid_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

def ex_gcd(a, m): # Убеждаемся, что E и значение функции Эйлера взаимно простые
    d = evklid_gcd(a, m)
    a0, a1 = a, m
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while a1 != 0:
        q = a0 // a1
        a0, a1 = a1, a0 - a1 * q
        x0, x1 = x1, x0 - x1 * q
        y0, y1 = y1, y0 - y1 * q
    return a0, x0

def prepare(message_list): # Функция для отображения списка в виде строки
    str = ''
    for i in message_list:
        str += i
    return str

def rsa(message, abc, p, q, e):
    n = p * q
    euler = (p-1) * (q-1)  # Вычисляем функцию Эйлера
    e = e  # Открытая экспонента
    a, x = ex_gcd(e, euler)
    d = (a * x) % euler  # Cекретная экспонента

    encrypted_text = rsa_enc(message, abc, e, n)
    decrypted_text = rsa_dec(encrypted_text, abc, d, n)

    return encrypted_text, decrypted_text

def rsa_enc(message, abc, e, n): # Каждый символ представляем в виде трехзначного числа, т.е. 11 - это 011
    numeric = [abc.index(i) + 1 for i in list(message)] # Составляем список индексов символов текста в алфавите
    return [(i ** e) % n for i in numeric] # Для каждого символа текста возводим его в степень E по модулю N

def rsa_dec(message, abc, d, n):
    plain = [(i ** d) % n for i in message] # Возводим символы зашифрованного текста в степень D по модулю N
    text = []
    for i in plain: # Переводим символы-индексы обратно в текстовые символы
        if (i - 1 + n) <= len(abc):
            text.append(abc[i - 1 + n])
        else:
            text.append(abc[i - 1])
    return text
    

print("Поговорка: " + pogovorka) # Проверяем на поговорке
encrypted = rsa(pogovorka, list_old_alphabet, 11, 19, 17)
print("Зашифрованное сообщение: " + str(encrypted[0]) + "\n" + "Расшифрованное сообщение: " + prepare(encrypted[1]))

str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
encrypted1 = rsa(str1, list_full_alphabet, 7, 13, 29)
print("Зашифрованное сообщение: " + str(encrypted1[0]) + "\n" + "Расшифрованное сообщение: " + prepare(encrypted1[1]))
input("Нажмите Enter, чтобы закрыть программу.")
