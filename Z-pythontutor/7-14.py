"""
Задача «Уникальные элементы»
Условие
Дан список. Выведите те его элементы, 
которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, 
в котором они встречаются в списке.

"""
# ???
s = input("imput string:")
A1 = s.split()
A = list(map(int, A1))
n = len(A)
A2 = []
for i in range(n):
    for j in range(i+1, len(A)):
        if i != j and A[i] == A[j]:
            A2.append(A[i])
for i in range(n):
    if A[i] not in A2:
        print(A[i])

# print(A)
# print(A2)
# print(len(A2))
