"""
Задача «Больше предыдущего»
Условие
Дан список чисел. Выведите все элементы списка, 
которые больше предыдущего элемента.

"""
A = []
s = None
s = input("imput string:")
A = s.split()

for i in range(1, len(A)):
    if int(A[i]) > int(A[i-1]):
        print(A[i])