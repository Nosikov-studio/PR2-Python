"""
Задача «Угадай число»
Условие
Август и Беатриса играют в игру. 
Август загадал натуральное число от 1 до n. 
Беатриса пытается угадать это число, 
для этого она называет некоторые множества натуральных чисел. 
Август отвечает Беатрисе YES, 
если среди названных ей чисел есть задуманное 
или NO в противном случае. 
После нескольких заданныъх вопросов Беатриса запуталась в том, 
какие вопросы она задавала и какие ответы получила 
и просит вас помочь ей определить, 
какие числа мог задумать Август.

В первой строке задано n - максимальное число, 
которое мог загадать Август. 
Далее каждая строка содержит вопрос Беатрисы 
(множество чисел, разделенных пробелом) 
и ответ Августа на этот вопрос.

Вы должны вывести через пробел, 
в порядке возрастания, все числа, которые мог задумать Август.

"""
a = None
M = []
n = int(input('max:'))
s = {i for i in range(1, n+1)}
# print(s)

while a != "HELP":
    a = input('input series:')
    if a == 'HELP':
        break
    promt = input('input promt:')

    ams = a.split()
    amn = [int(i) for i in ams]
    amns = set(amn)
    if promt == "NO":
        s -= amns
    if promt == "YES":
        s = s & amns


# print(M)
M = list(s)
MS = [str(i) for i in M]
ms = " ".join(MS)
print(ms)
