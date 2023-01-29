import random
import sys

############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк" 

################## ГОСТ Р 34.10-94 подпись ##################
print("\n################## ГОСТ Р 34.10-94 подпись ##################\n")

list_old_alphabet = [] # Составляем список для алфавита формата ['a', 'б', ...]
for i in old_alphabet:
    list_old_alphabet.append(i)
list_full_alphabet = [] # То же самое для расширенного алфавита
for i in full_alphabet:
    list_full_alphabet.append(i)

def hash_square(len_of_message, message, abc, P):
    if len_of_message == 0: # Если длина сообщения равна 0
        return 0
    h = 0
    for sumbol in message:
        sumbol = abc.index(sumbol)
        h = (h + sumbol ** 2) % 22
    return h

def GOST_R_34_10_94(abc, message, P, Q, A, X, K):
    if X == 0:
        X = random.randint(1, Q) # Генерируем случайное число x, меньшее Q
    Y = A ** X % P
    if K == 0:
        K = random.randint(1, 1000) # Генерируем случайное число k

    # Цифровая подпись представляет собой два числа: R и S
    R = (A ** K % P) % Q
    S = (X * R + K * hash_square(len(message), message, abc, P)) % Q

    print('R =', R % (2 ** 256), ', S =', S % (2 ** 256))
    return R, S, Q, A, Y, P, message

def check(abc, R, S, Q, A, Y, P, message):
    # Проверяем полученную подпись, вычисляя:
    V = hash_square(len(message), message, abc, P) ** (Q - 2) % Q
    Z1 = (S * V) % Q
    Z2 = ((Q - R) * V) % Q
    U = ((A ** Z1 * Y ** Z2) % P) % Q
    print(V, Z1,Z2,U)
    if U == R:
        print(U, "равен", R)
        print('Цифровая подпись подтверждена.')
    else:
        print(U, "не равен", R)
        print('Цифровая подпись не подтверждена.')

# Определяем P, Q и A. 
# P = random.randint(1, 1000) # Можем воспользоваться рандомайзером
# Q = random.randint(1, 1000)
# A = random.randint(1, 1000)

P = 23
Q = 11
A = 6
X = 4
K = 5

if A ** Q % P != 1: # Проверка числа A
    print("A^Q mod P должно быть равно 1.")
    sys.exit()

print('P = ', P, ', Q = ', Q, ', A = ', A)
print("Сообщение: ", pogovorka)
result = GOST_R_34_10_94(list_old_alphabet, pogovorka, P, Q, A, X, K)
check(list_old_alphabet, result[0], result[1], result[2], result[3], result[4], result[5], result[6])

str1 = input("Введите сообщение: ") # Проверяем на тексте в 1000 символов с полным алфавитом
result1 = GOST_R_34_10_94(list_full_alphabet, str1, P, Q, A, 0, 0)
check(list_full_alphabet, result1[0], result1[1], result1[2], result1[3], result1[4], result1[5], result1[6])
input("Нажмите Enter, чтобы закрыть программу.")
