"""
Задача «Стоимость покупки»
Условие
Пирожок в столовой стоит a рублей и b копеек.
Определите, сколько рублей и копеек нужно заплатить за n пирожков. 
Программа получает на вход три числа: a, b, n, 
и должна вывести два числа: стоимость покупки в рублях и копейках.

"""
a = int(input("input a:"))
b = int(input("input b:"))
n = int(input("input n:"))

r = n*a+(n*b)//100
c = (n*b) % 100

print(r, c)
