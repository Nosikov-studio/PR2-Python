"""
Задача «Утренняя пробежка»
Условие
В первый день спортсмен пробежал x километров, 
а затем он каждый день увеличивал пробег 
на 10% от предыдущего значения. 
По данному числу y определите номер дня, 
на который пробег спортсмена составит не менее y километров.

Программа получает на вход действительные числа x и y 
и должна вывести одно натуральное число.

"""
x0 = float(input("input x:"))
y = float(input("input y:"))
# x1=x0+x0*(1/10)

x = x0
n = 1
while x < y:
    x = x+x*(1/10)
    n += 1
print(n)