"""
Задача «Поменять столбцы»
Условие
Дан двумерный массив и два числа: i и j. 
Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, 
затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j).

"""
n, m = [int(i) for i in input().split()]
M = [[int(j) for j in input().split()] for i in range(n)]
i1, j1 = [int(i) for i in input().split()]


def swap_columns(a, i, j):
    sti = [0]*n
    stj = [0]*n
    for k in range(n):
        sti[k] = a[k][i]
        stj[k] = a[k][j]
        a[k][i] = stj[k]
        a[k][j] = sti[k]
    return a


def ras(A):
    for i in range(n):
        st = ""
        for j in range(m):
            st += str(A[i][j])
            st += " "
        print(st)


ras(swap_columns(M, i1, j1))
