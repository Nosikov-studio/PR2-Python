"""
Задача «Наибольший элемент»
Условие
Дан список чисел. Выведите значение наибольшего элемента в списке,
 а затем индекс этого элемента в списке. 
 Если наибольших элементов несколько, 
 выведите индекс первого из них.

"""
A = []
s = None
m = None
ind = 0
s = input("imput string:")
A = s.split()
m = int(A[0])
for i in range(0, len(A)):

    if int(A[i]) > m:
        m = int(A[i])
        ind = i

print(m, ind)
