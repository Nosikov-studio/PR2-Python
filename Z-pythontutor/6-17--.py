"""
Задача «Стандартное отклонение»
Условие
Дана последовательность натуральных чисел x1, x2, ..., xn. 
<...>
Определите стандартное отклонение для данной последовательности 
натуральных чисел, завершающейся числом 0.

"""
# ????????????????????????????????????????????????
s = 0
n = None
sum = 0
count = 0
while n != 0:
    n = int(input("imput number:"))
    if n != 0:
        count += 1
        sum += n
    globals()["x"+str(count)] = n
s = sum / count
# Можно ли создавать имена переменных в цикле ???
# Динамические имена переменных ????
# locals()["x"+str(count)]=n
# globals()["x"+str(count)]=n
# Функция globals() выдает словарь глобальных переменных (ключ – имя переменной).
# Функция locals() возвращает словарь только локальных переменных.
for i in range(0, count):
    print("x"+str(i))

print(s)