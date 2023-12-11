"""
Задача «Отрицательная степень»
Условие
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.

"""
a1 = float(input("a:"))
n1 = int(input("n:"))

# result = 1


def power(a, n):
    result = 1
    if n == 0:
        result = 1
        return 1
    elif n > 0:
        for i in range(n):
            result = result*a
        return result
    elif n < 0:
        for i in range(-n):
            result = result*a
        return float(1/result)


print(power(a1, n1))
