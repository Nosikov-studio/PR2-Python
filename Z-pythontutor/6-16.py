"""
Задача «Максимальное число идущих подряд равных элементов»
Условие
Дана последовательность натуральных чисел, 
завершающаяся числом 0. 
Определите, какое наибольшее число подряд идущих элементов 
этой последовательности равны друг другу.

"""
# ????????????????????????????????????????????????
n = None
p = None
count1 = 1
count2 = 1

while n != 0:
    n = int(input("imput number:"))
    if n != 0:
        if n == p:
            count1 += 1
        elif (n != p):
            if count1 > count2:
                count2 = count1
                count1 = 1
            count1 = 1
    else:
        if n == p:
            count1 += 1
        elif (n != p):
            if count1 > count2:
                count2 = count1
                count1 = 1
            count1 = 1

    p = n

print(count2)
