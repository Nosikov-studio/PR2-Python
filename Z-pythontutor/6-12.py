"""
Задача «Второй максимум»
Условие
Последовательность состоит из различных натуральных чисел 
и завершается числом 0. 
Определите значение второго по величине элемента 
в этой последовательности. 
Гарантируется, что в последовательности есть хотя бы два элемента.
"""
n = None
m1 = 0
m2 = 0


while n != 0:
    n = int(input("imput number:"))
    if n != 0:
        if n > m1:
            m2 = m1
            m1 = n
        else:
            if n > m2:
                m2 = n


print(m2)
