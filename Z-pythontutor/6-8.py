"""
Задача «Максимум последовательности»
Условие
Последовательность состоит из натуральных чисел 
и завершается числом 0. 
Определите значение наибольшего элемента последовательности.

"""

n = None
m = 0

while n != 0:
    n = int(input("imput number:"))
    if n != 0:
        if n > m:
            m = n


print(m)
