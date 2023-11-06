"""
Задача «Яша плавает в бассейне»
Условие
Яша плавал в бассейне размером N × M метров и устал.
 В этот момент он обнаружил, 
 что находится на расстоянии x метров от одного из длинных бортиков 
 (не обязательно от ближайшего) 
 и y метров от одного из коротких бортиков. 
 Какое минимальное расстояние должен проплыть Яша, 
 чтобы выбраться из бассейна на бортик? 
 Программа получает на вход числа N, M, x, y. 
 Программа должна вывести число метров, 
 которое нужно проплыть Яше до бортика.


"""
N = int(input("input N:"))
M = int(input("input M:"))
x = int(input("input x:"))
y = int(input("input y:"))
xmin = 0
ymin = 0
if (M > N):
    xmin = min(x, N-x)
    ymin = min(y, M-y)
else:
    xmin = min(x, M-x)
    ymin = min(y, N-y)

Lmin = min(xmin, ymin)

print(Lmin)
