"""
Задача «Ход ладьи»
Условие
Шахматная ладья ходит по горизонтали или вертикали. 
Даны две различные клетки шахматной доски, определите, 
может ли ладья попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. 
Программа должна вывести YES, 
если из первой клетки ходом ладьи можно попасть во вторую 
или NO в противном случае.

"""
ax = int(input("input column a:"))
ay = int(input("input row a:"))
bx = int(input("input column b:"))
by = int(input("input row b:"))

if (ax == bx or ay == by):
    print("YES")
else:
    print("NO")