"""
Задача «Переставить min и max»
Условие
В списке все элементы различны. 
Поменяйте местами минимальный и максимальный элемент этого списка.
"""
s = input("imput string:")
A1 = s.split()
A = list(map(int, A1))
# print(A)
n = len(A)


m1 = min(A)
m2 = max(A)
ind1 = A.index(m1)
ind2 = A.index(m2)

A[ind1], A[ind2] = A[ind2], A[ind1]

# print(A)
for i in range(0, n):
    print(A[i])
