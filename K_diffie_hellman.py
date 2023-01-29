import random

############# Используемые алфавиты ############
old_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
full_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!\"#$%&\'()*+-—«».,<>?/|\\;:№_=[]{}`~1234567890 АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя€ˈ“”…"

pogovorka = "плохойработникникогданенаходитхорошегоинструментатчк" 

################## Обмен ключами по ДИФФИ-ХЕЛЛМАНУ ##################
print("\n################## Обмен ключами по ДИФФИ-ХЕЛЛМАНУ ##################\n")

def Alice_key(N, A, Ka):
    if Ka == 0:
        Ka = random.randint(2, N - 1) # Берем случайное число Ka 
    Ya = (A ** Ka) % N # Вычисляем открытый ключ Y1
    print('Открытый ключ Алисы Ya = ', Ka, '. Секретный ключ Алисы Ka = ', Ya)
    return Ya, Ka

def Bob_key(N, A, Kb):
    if Kb == 0:
        Kb = random.randint(2, N - 1) # Берем случайное число Kb 
    Yb = (A ** Kb) % N # Вычисляем открытый ключ Y2
    print('Открытый ключ Боба Yb = ', Yb, '. Секретный ключ Боба Kb = ', Kb)
    return Yb, Kb

def Alice_check(N, Ya, Yb, Ka):
    K = (Yb ** Ka) % N
    return K

def Bob_check(N, Ya, Yb, Kb):
    K = (Ya ** Kb) % N
    return K

def diffie_hellman(K1, K2):
    print('Общий ключ Алисы K1 = ', K1, '. Общий ключ Боба K2 = ', K2)
    if K1 == K2:
        print('Ключи равны.')
    else:
        print('Ключи не равны.')


# Определяем известные всем числа A и N, такие, что 1 < A < N
N = input('Введите число N: ') # N = 46
temp = 0
while temp == 0: # Проверяем введенное значение, оно должно быть числом, большим единицы
    if not N.isnumeric():
        N = input('N должно быть числом. Введите N: ')
    else:
        if int(N) > 1:
            temp = 1
        else:
           N = input('N должно быть числом, большим единицы. Введите N: ') 
A = input('Введите число A, меньшее N: ') # A = 15
while temp == 1:
    if not A.isnumeric():
        A = input('A должно быть числом. Введите A: ')
    else:
        if int(A) > 1 and int(A) < int(N): # Проверяем, что 1 < A < N
            temp = 0
        else:
           A = input('A должно быть числом, большим единицы и меньшим N = {}. Введите A: '.format(N))
N = int(N)
A = int(A)

print('\nЧисло N = ', N, '. Число A = ', A)
Alice_keys = Alice_key(N, A, 8)
Bob_keys = Bob_key(N, A, 14)
print('Обмен открытыми ключами...')
diffie_hellman(Alice_check(N, Alice_keys[0], Bob_keys[0], Alice_keys[1]), Bob_check(N, Alice_keys[0], Bob_keys[0], Bob_keys[1]))
input("Нажмите Enter, чтобы закрыть программу.")
