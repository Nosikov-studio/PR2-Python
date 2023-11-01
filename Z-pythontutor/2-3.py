"""
Задача «Шахматная доска»
Условие
Заданы две клетки шахматной доски. 
Если они покрашены в один цвет, то выведите слово YES, 
а если в разные цвета — то NO. 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, 
потом для второй клетки.

"""
ax = int(input("input column a:"))
ay = int(input("input row a:"))
bx = int(input("input column b:"))
by = int(input("input row b:"))


def cl(x, y):
    if x % 2 == y % 2:
        return "b"
    else:
        return "w"


if cl(ax, ay) == cl(bx, by):
    print("YES")
else:
    print("NO")
