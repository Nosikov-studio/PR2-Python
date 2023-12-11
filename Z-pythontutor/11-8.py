"""
Задача «Англо-латинский словарь»
https://pythontutor.ru/lessons/dicts/problems/english_latin_dict/

"""
s = []
d = dict()
dlat = dict()
s1 = []
n = int(input("n:"))
lat = set()
for i in range(n):
    s1 = (input("input:").split(' - '))
    s2 = s1[1].split(', ')
    d[s1[0]] = s2
    lat = lat | set(s2)
L = list(lat)
L.sort()
# print(d)
# print(lat)
# print(L)
print(len(L))
for i in range(len(L)):
    for key, value in d.items():
        if (L[i] in value) and (L[i] not in dlat):
            dlat[L[i]] = [key]
        elif (L[i] in value) and (L[i] in dlat):
            dlat[L[i]] += [key]
    ls1 = L[i]
    ls2 = ", ".join(dlat[L[i]])

    print(ls1, "-", ls2)
