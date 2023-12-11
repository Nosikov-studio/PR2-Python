"""
Задача «Побочная диагональ»
Условие
Дано число n. Создайте массив размером n×n 
и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего 
в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. 
Числа в строке разделяйте одним пробелом.
"""
n = int(input("imput n:"))

M = [['' for i in range(n)] for j in range(n)]


def ras(A):
    for i in range(n):
        st = ""
        for j in range(n):
            st += str(A[i][j])
            st += " "
        print(st)


#
for i in range(n):
    for j in range(n):
        if (i+j == n-1):
            M[i][j] = 1
        if (i+j < n-1):
            M[i][j] = 0
        if (i+j > n-1):
            M[i][j] = 2


# print(M)
ras(M)