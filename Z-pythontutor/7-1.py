"""
Задача «Четные индексы»
Условие
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

"""

A = []
s = None
# while n != 0:
#     n = int(input("imput number:"))
#     A.append(n)

# A = [input() for i in range(int(input()))]
s = input("imput string:")
A = s.split()


for i in range(len(A)):
    if i % 2 == 0:
        print(A[i])
