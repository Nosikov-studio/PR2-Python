"""
Задача «Контрольная по ударениям»
https://pythontutor.ru/lessons/dicts/problems/accent_test/

"""
# функция, которая считает количество заглавных букв в слове


def nz(word):
    counter = 0
    for ch in word:
        if ch.isupper():
            counter += 1
    return counter


# **************************************************
d = dict()
P = []
n = int(input("input n:"))
for i in range(n):
    s = input("dict word:")
    s1 = s.lower()
    if s1 not in d:
        d[s1] = []
        d[s1].append(s)
    else:
        d[s1].append(s)
k = input("Peta test:")
P = k.split()
# print(d)
# print(P)
w = 0
r = 0
for i in P:
    if i == i.lower():
        w += 1
    elif i.lower() in d:
        if i not in d[i.lower()]:
            w += 1
    elif nz(i) > 1:
        w += 1


print(w)
