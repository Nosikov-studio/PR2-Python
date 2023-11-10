"""
Задача «Ряд - 1»
Условие
Даны два целых числа A и B (при этом A ≤ B). 
Выведите все числа от A до B включительно.
"""
a = int(input("input a:"))
b = int(input("input b:"))

for i in range(a, b+1):
    print(i)
