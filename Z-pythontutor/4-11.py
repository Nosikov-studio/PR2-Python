"""
Задача «Потерянная карточка»
Условие
Для настольной игры используются карточки с номерами от 1 до N.
 Одна карточка потерялась. 
 Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек 
(различные числа от 1 до N). 
Программа должна вывести номер потерянной карточки.

Для самых умных: 
массивами и аналогичными структурами данных пользоваться нельзя.

"""
s1 = 0
n = int(input("Введите число чисел:"))
s = int(n*(n+1)/2)

for i in range(n-1):
    s1 += int(input("Введите текущее число:"))

x = s-s1
print(x)
