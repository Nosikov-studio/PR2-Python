"""
Задача «Ход слона»
Условие
Шахматный слон ходит по диагонали. 
Даны две различные клетки шахматной доски, определите, 
может ли слон попасть с первой клетки на вторую одним ходом.

"""

ax = int(input("input column a:"))
ay = int(input("input row a:"))
bx = int(input("input column b:"))
by = int(input("input row b:"))

c1 = ay-ax
c2 = ay+ax

if (by-bx == c1 or by+bx == c2):
    print("YES")
else:
    print("NO")
