"""
Задача «Права доступа»
https://pythontutor.ru/lessons/dicts/problems/permissions/

"""
s = []
d = dict()
s1 = []
n = int(input("n:"))
for i in range(n):
    d1 = {'read': 'NO', 'write': 'NO', 'execute': 'NO'}
    s1 = (input().split())
    if 'W' in s1:
        d1['write'] = 'YES'
    if 'R' in s1:
        d1['read'] = 'YES'
    if 'X' in s1:
        d1['execute'] = 'YES'
    d[s1[0]] = d1

# print(d)

m = int(input("m:"))
for i in range(m):
    s2 = (input().split())
    if d[s2[1]][s2[0]] == 'YES':
        print("OK")
    else:
        print("Access denied")
