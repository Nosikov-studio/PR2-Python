"""
Задача «Улитка»
Условие
Улитка ползет по вертикальному шесту высотой h
метров, поднимаясь за день на a метров, 
а за ночь спускаясь на b метров. 
На какой день улитка доползет до вершины шеста?

Программа получает на вход натуральные числа h, a, b.

Программа должна вывести одно натуральное число. 
Гарантируется, что a>b.
?????????????????????????????
"""
import math
h = int(input("input h:"))
a = int(input("input a:"))
b = int(input("input b:"))

# Достижением (пиком восхождения) дня будет: hx=n*a-(n-1)*b
# где n - номер дня
# hx>=h или h <= n*a-n*b+b
# отсюда n >= (h-b)/(a-b)
d = math.ceil((h-b)/(a-b))
print(d)
