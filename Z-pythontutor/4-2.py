"""
Задача «Ряд - 2»
Условие
Даны два целых числа A и В. 
Выведите все числа от A до B включительно, в порядке возрастания, 
если A < B, или в порядке убывания в противном случае.
"""
a = int(input("input a:"))
b = int(input("input b:"))

if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
