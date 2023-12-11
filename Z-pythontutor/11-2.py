"""
Задача «Словарь синонимов»
Условие
Вам дан словарь, состоящий из пар слов. 
Каждое слово является синонимом к парному ему слову. 
Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, 
определите его синоним.

"""
d1 = dict()
d2 = dict()
n = int(input("n:"))
for i in range(n):
    x, y = [j for j in input("input 2 words:").split()]
    d1[x] = y
    d2[y] = x

s = input("input word:")

if s in d1:
    print(d1[s])
if s in d2:
    print(d2[s])


# print(d1)
# print(d2)
