"""
Задача «Ход ферзя»
Условие
Шахматный ферзь ходит по диагонали, горизонтали или вертикали. 
Даны две различные клетки шахматной доски, определите, 
может ли ферзь попасть с первой клетки на вторую одним ходом.

"""
ax = int(input("input column a:"))
ay = int(input("input row a:"))
bx = int(input("input column b:"))
by = int(input("input row b:"))

c1 = ay-ax
c2 = ay+ax

if (by-bx == c1 or by+bx == c2 or ax == bx or ay == by):
    print("YES")
else:
    print("NO")
