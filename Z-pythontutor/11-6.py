"""
Задача «Частотный анализ»
https://pythontutor.ru/lessons/dicts/problems/frequency_analysis/

"""
s = []
d = dict()
s1 = []
n = int(input("n:"))
for i in range(n):
    s1 = (input().split())
    s += s1
# print(s)


for i in range(len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

M = []
for key, value in d.items():
    M.append((value, key))

sM = sorted(M, key=lambda x: (-x[0], x[1]))
# print(sM)
for i in sM:
    print(i[1])
