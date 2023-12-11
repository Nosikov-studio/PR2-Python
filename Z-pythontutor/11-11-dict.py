D = {'Alexei': 'Petr', 'Anna': 'Petr', 'Eliza': 'Petr', 'P2': 'Alexei',
     'P3': 'Anna', 'Paul': 'P3', 'Alex': 'Paul', 'Nikola': 'Paul'}
n = 9
m = n-1
s = [['Alexei', 'Petr'], ['Anna', 'Petr'], ['Eliza', 'Petr'], ['P2', 'Alexei'], [
    'P3', 'Anna'], ['Paul', 'P3'], ['Alex', 'Paul'], ['Nikola', 'Paul']]

p = set()
p2 = set()

for i in range(n-1):
    # st = input("child, parent:").split()
    # s.append(st)
    # st1 = set(st)
    # st2 = st[0]
    p = p.union(set(s[i]))
    p2.add(s[i][0])
# print(s)
# p - множество всех людей из списка
# print(p)
# p2 - множество потомков
# print(p2)

# находим прародителя r0
r = p-p2
r0 = list(r)[0]
# print(r0)
# список всех людей (упорядоченный)
pls = list(p)
pls.sort()
# создадим два словаря
# 1)pl чел - и его дети
# 2)fl чел - и его порядковый номер в родословной (пока для всех неизвестен -1)
pl = dict()
fl = dict()
for i in range(len(p)):
    pl[pls[i]] = []
    fl[pls[i]] = -1
    for j in range(n-1):
        if pls[i] == s[j][1]:
            pl[pls[i]].append(s[j][0])

# print(pl)
# print(fl)
# отметим во втором словаре fl только прародителя
for i in range(len(p)):
    if pls[i] == r0:
        fl[pls[i]] = 0
# print(fl)
# найдём по заданному значению номера поколения все ключи во втором словаре


def per(m):
    g = []
    for k, v in (fl.items()):
        if v == m:
            g.append(k)
    g.sort()
    return g


# print(per(0))
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
    # for i in range(len(pl[x])):
    #     k = pl[x][i]
    fl[k] = m


# lev('p', 2)
# print(b)
print("******************************************")

# print(gen(per(0)))
i = 0

while len(p) != 0:
    pr = []
    # print(i)
    pr = per(i)
    # нужно получить список детей этих родителей
    g = gen(per(i))
    i += 1
    for j in range(len(g)):
        lev(g[j], i)
    # print(g)
    # print(pr)
    p.pop()


# print(p)
# p.discard('P3')
# print(p)

# print(fl)
for k, v in fl.items():
    print(k, v)
