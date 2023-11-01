"""
Задача «Минимум из трех чисел»
Условие
Даны три целых числа. Выведите значение наименьшего из них.

"""
a = int(input("input a:"))
b = int(input("input b:"))
c = int(input("input c:"))

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
elif c <= a and c <= b:
    print(c)
else:
    ("What?")
