"""
Задача «Степень двойки»
Условие
По данному натуральному числу N 
найдите наибольшую целую степень двойки, не превосходящую N. 
Выведите показатель степени и саму степень.

Операцией возведения в степень пользоваться нельзя!
"""
N = int(input("input N:"))
# 2**x <=N
x = 0

while 2**x <= N:
    if 2**(x+1) > N:
        print(x, 2**x)
    x += 1
