"""
Задача «Ход коня»
Условие
Шахматный конь ходит буквой “Г” 
— на две клетки по вертикали в любом направлении 
и на одну клетку по горизонтали, или наоборот. 
Даны две различные клетки шахматной доски, определите, 
может ли конь попасть с первой клетки на вторую одним ходом.


"""
ax = int(input("input column a:"))
ay = int(input("input row a:"))
bx = int(input("input column b:"))
by = int(input("input row b:"))

if ((abs(ax-bx) == 1 and abs(ay-by) == 2) or (abs(ax-bx) == 2 and abs(ay-by) == 1)):
    print("YES")
else:
    print("NO")
