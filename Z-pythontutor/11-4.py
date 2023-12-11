"""
Задача «Самое частое слово»
Условие
Дан текст: в первой строке задано число строк, 
далее идут сами строки. Выведите слово, 
которое в этом тексте встречается чаще всего. 
Если таких слов несколько, выведите то, 
которое меньше в лексикографическом порядке.

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

# print(d)
vmx = 0
kmx = ""
for key, val in d.items():
    if val > vmx:
        kmx = key
        vmx = val
    if val == vmx and key < kmx:
        kmx = key
        vmx = val

print(kmx)
