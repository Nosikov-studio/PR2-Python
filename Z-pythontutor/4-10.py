"""
Задача «Лесенка»
Условие
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, 
i-я ступенька состоит из чисел от 1 до i без пробелов.

"""

st = ''
n = int(input("Введите число чисел:"))

for i in range(1, n+1):

    st += str(i)
    print(st)
