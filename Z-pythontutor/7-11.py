"""
Задача «Удалить элемент»
Условие
Дан список из чисел и индекс элемента в списке k. 
Удалите из списка элемент с индексом k,
 сдвинув влево все элементы, 
 стоящие правее элемента с индексом k.

Программа получает на вход список, затем число k.
Программа сдвигает все элементы, 
а после этого удаляет последний элемент списка 
при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, 
а не делать это при выводе элементов. 
Также нельзя использовать дополнительный список. 
Также не следует использовать метод pop(k) с параметром.

"""
s = input("imput string:")
k = int(input("k:"))
A1 = s.split()
A = list(map(int, A1))
# print(A)
n = len(A)
for i in range(k, n-1):
    A[i] = A[i+1]
A.pop()

# print(A)
for i in range(0, len(A)):
    print(A[i])