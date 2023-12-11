"""
Задача «Страны и города»
Условие
Дан список стран и городов каждой страны. 
Затем даны названия городов. 
Для каждого города укажите, в какой стране он находится.

"""
s = []
d = dict()
s1 = []
n = int(input("country n:"))
for i in range(n):
    s1 = (input("country and cities:").split())
    d[s1[0]] = s1

m = int(input("cities m:"))
for i in range(m):
    s2 = input("city:")
    for key, value in d.items():
        if s2 in value:
            print(key)


# print(d)
