"""
Задача «Шеренга»
Условие
Петя перешёл в другую школу.
На уроке физкультуры ему понадобилось 
определить своё место в строю. 
Помогите ему это сделать.
Программа получает на вход 
невозрастающую последовательность натуральных чисел, 
означающих рост каждого человека в строю. 
После этого вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. 
Если в строю есть люди с одинаковым ростом, 
таким же, как у Пети, то он должен встать после них.

"""
s = input("imput string:")
A = s.split()
x = int(input("x:"))
m = int(A[0])

n = 0
for i in range(0, len(A)):

    if int(A[i]) < x:
        n = i+1
        break
    else:
        n = len(A)+1

print(n)
