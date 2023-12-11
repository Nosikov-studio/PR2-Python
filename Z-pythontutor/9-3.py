"""
Задача «Шахматная доска»
Условие
Даны два числа n и m. 
Создайте двумерный массив размером n×m 
и заполните его символами "." и "*" в шахматном порядке. 
В левом верхнем углу должна стоять точка.

"""
n, m = [int(i) for i in input().split()]

M = [['' for i in range(m)] for j in range(n)]


def ras(A):
    for i in range(n):
        st = ""
        for j in range(m):
            st += A[i][j]
            st += " "
        print(st)


for i in range(n):
    for j in range(m):
        if ((i % 2 == 0) and (j % 2 == 0)) or ((i % 2 != 0) and (j % 2 != 0)):
            M[i][j] = '.'
        else:
            M[i][j] = '*'

# print(M)
ras(M)
