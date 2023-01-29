############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк" 

################## Алгоритм цифровых подписей ELGAMAL ##################
print("\n################## Алгоритм цифровых подписей ELGAMAL ##################\n")

def hash_square(len_of_message, message, abc): # Функция для вычисления hash
    if len_of_message == 0: # Если длина сообщения равна 0
        return 0
    h = 0
    k = 0
    for sumbol in message:
        k += 1
        sumbol = abc.index(sumbol)
        h = (h + sumbol ** 2) % 22
    return h

def hi(n: int) -> int: # Функция для вычисления B
    result = n
    i = 2
    while i ** 2 < n:
        while n % i == 0:
            n /= i
            result -= result / i
        i += 1
    if n > 1:
        result -= result / n
    return result

def elgamal(message, abc):
    if abc == 1:
        list_alphabet = [] # Составляем список для алфавита формата ['a', 'б', ...]
        for i in old_alphabet:
            list_alphabet.append(i)
    if abc == 2:
        list_alphabet = []
        for i in full_alphabet:
            list_alphabet.append(i)

    h = hash_square(len(message), message, list_alphabet)
    P = 23 # Большое простое целое число
    G = 5 # Большое целое число, G < P
    X = 13 # Случайное целое число
    Y = G ** X % P
    K = 7 # Случайное целое число, 1 < К < (Р-1), К и (Р-1) - взаимно простые
    A = G ** K % P
    B = int(((h - A * X) * K ** (hi(P-1) - 1)) % (P-1))
    return message, list_alphabet, Y, A, B, P, G, X


def check(message, abc, y, a, b, p, g):
    h = hash_square(len(message), message, abc)
    A1 = (y ** a * a ** b) % p
    A2 = g ** h % p
    if A1 == A2:
        print(A1, "равен", A2)
        print('Цифровая подпись подтверждена.')
    else:
        print(A1, "не равен", A2)
        print('Цифровая подпись не подтверждена.')

text = elgamal(pogovorka, 1)
print("Сообщение: ", pogovorka)
print("Открытый ключ Y =", text[2], "\nЗакрытый ключ X =", text[7], "\n", text[3], text[4])
check(text[0], text[1], text[2], text[3], text[4], text[5], text[6])

str1 = input("\nВведите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
text2 = elgamal(str1, 2)
print("Открытый ключ Y =", text2[2], "\nЗакрытый ключ X =", text2[7], "\n", text2[3], text2[4])
check(text2[0], text2[1], text2[2], text2[3], text2[4], text2[5], text2[6])
input("Нажмите Enter, чтобы закрыть программу.")
