"""
Условие
В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x). 
Эту задачу желательно решить с использованием каскадных инструкций
 if... elif... else.

"""
a = int(input("input a:"))


def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        print("noooo!!!")


print(sign(a))
