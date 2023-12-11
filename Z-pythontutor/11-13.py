"""
Задача «Родословная: LCA»


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


D = dict(s)
# print(D)

s2 = []
k = int(input("k:"))
for i in range(k):
    st = input("person1 person2:").split()
    s2.append(st)

# print(s2)
# является ли предком, lev_p1 < lev_p2
# Превращение исходного списка в словарь


def a(p1, p2):
    lev_p1 = fl[p1]
    # print(lev_p1)
    lev_p2 = fl[p2]
    # print(lev_p2)
    r = lev_p2 - lev_p1
    t1 = p1
    t2 = p2
    for i in range(r):
        t2 = D[t2]
    # print(t)
    # print(fl[t])
    if t2 == p1:
        return t2
    else:
        while t2 != t1:
            t1 = D[t1]
            t2 = D[t2]
        if t1 == t2:
            return t2

# если на одном уровне


def ar(p1, p2):
    lev_p1 = fl[p1]
    # print(lev_p1)
    lev_p2 = fl[p2]
    t1 = p1
    t2 = p2
    while t2 != t1:
        t1 = D[t1]
        t2 = D[t2]
    if t1 == t2:
        return t2


# a('Petr', 'Paul')
# найдем функцию определяющего "предковость"


def anc(a1, a2):
    # print(a1)
    # print(a2)
    lev_a1 = int(fl[a1])
    lev_a2 = int(fl[a2])
    if lev_a1 > lev_a2:
        return a(a2, a1)
    elif lev_a2 > lev_a1:
        return a(a1, a2)
    elif lev_a2 == lev_a1:
        return ar(a1, a2)


for i in range(k):
    result = anc(s2[i][0], s2[i][1])
    print(result)
