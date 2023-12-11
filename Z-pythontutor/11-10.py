"""
Задача «Продажи»


"""
from sys import stdin

s = []
for line in stdin:
    s.append(line.split())


setp = set()
sett = set()

for i in range(len(s)):
    setp.add(s[i][0])
    sett.add(s[i][1])


sp = list(setp)
st = list(sett)
sp.sort()
st.sort()
d = dict()


for i in range(len(sp)):
    d[sp[i]] = dict()
    for j in range(len(st)):
        d[sp[i]][st[j]] = 0


for i in range(len(s)):
    p = s[i][0]
    t = s[i][1]
    n = int(s[i][2])
    d[p][t] += n


for i in range(len(sp)):
    print(sp[i].strip() + ":")
    for j in range(len(st)):
        if d[sp[i]][st[j]] != 0:
            print(st[j], d[sp[i]][st[j]])
