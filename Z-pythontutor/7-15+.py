"""
Задача «Кегельбан»
Условие
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.

"""
s = input("imput string:")
A1 = s.split()
A = list(map(int, A1))

N = A[0]
K = A[1]

B = []
for i in range(K):
    s2 = input("Введите интервал:")
    A2 = s2.split()
    B += A2


LR = list(map(int, B))


R = ['I']*N

for i in range(1, K+1):
    l = LR[2*i-2]
    r = LR[2*i-1]
    for j in range(l, r+1):
        R[j-1] = '.'

str1 = ""
for i in range(N):
    str1 += str(R[i])

print(str1)
