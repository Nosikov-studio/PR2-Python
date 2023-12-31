"""
Задача «Ход короля»
Условие
Шахматный король ходит по горизонтали, 
вертикали и диагонали, но только на 1 клетку. 
Даны две различные клетки шахматной доски, определите, 
может ли король попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. 
Программа должна вывести YES, 
если из первой клетки ходом короля можно попасть во вторую 
или NO в противном случае.

"""
# import math
ax = int(input("input column a:"))
ay = int(input("input row a:"))
bx = int(input("input column b:"))
by = int(input("input row b:"))

if (abs(ax-bx) <= 1 and abs(ay-by) <= 1):
    print("YES")
else:
    print("NO")
