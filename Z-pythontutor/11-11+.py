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


def per(m):
    g = []
    for k, v in (fl.items()):
        if v == m:
            g.append(k)
    g.sort()
    return g


# ******************************************************************
# нужно получить список детей из списка родителей


def gen(p):
    g = []

    for i in range(len(p)):
        g += pl[p[i]]
    return g


# *******************************************************************
# получаем ключ словаря а и маркер-значение для отметки в словаре fl

def lev(k, m):

    fl[k] = m


# print("******************************************")

i = 0

while len(p) != 0:
    pr = []
    pr = per(i)
    # нужно получить список детей этих родителей
    g = gen(per(i))
    i += 1
    for j in range(len(g)):
        lev(g[j], i)

    p.pop()


for k, v in fl.items():
    print(k, v)
