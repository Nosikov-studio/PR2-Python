"""
Задача «Переставить соседние»
Условие
Переставьте соседние элементы списка 
(A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число, 
то последний элемент остается на своем месте.
"""
s = input("imput string:")
A = s.split()
n = len(A)
B = []

if n % 2 == 0:
    for i in range(0, len(A)-1):
        if i % 2 == 0:
            A[i], A[i+1] = A[i+1], A[i]

else:
    for i in range(0, len(A)-2):
        if i % 2 == 0:
            A[i], A[i+1] = A[i+1], A[i]

for i in range(0, n):
    print(A[i])
