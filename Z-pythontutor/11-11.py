"""
Задача «Родословная: подсчет уровней»
https://pythontutor.ru/lessons/dicts/problems/genealogy_level_count/
"""
s = []
p = set()
p2 = set()

n = int(input("n:"))
for i in range(n-1):
    st = input("child, parent:").split()
    s.append(st)
    st1 = set(st)
    st2 = st[0]
    p = p.union(st1)
    p2.add(st2)
print(s)
print(p)
print(p2)
r = p-p2
r0 = list(r)[0]
pls = list(p)
pls.sort()
pl = dict()
fl = dict()
for i in range(len(p)):
    pl[pls[i]] = []
    fl[pls[i]] = -1
    for j in range(n-1):
        if pls[i] == s[j][1]:
            pl[pls[i]].append(s[j][0])

for i in range(len(p)):
    if pls[i] == r0:
        fl[pls[i]] = 0

print(pl)
print(fl)


def lev(x, m):  # получаем ключ словаря а и маркер-значение для отметки в словаре b
    for i in range(len(pl[x])):
        k = pl[x][i]
        fl[k] = m


for i in range(len(p)):
    # ???????????????????????????????????????
