"""
Задача «Разность времен»
Условие
Даны значения двух моментов времени, 
принадлежащих одним и тем же суткам: 
часы, минуты и секунды для каждого из моментов времени. 
Известно, что второй момент времени наступил не раньше первого. 
Определите, сколько секунд прошло между двумя моментами времени.

Программа на вход получает три целых числа: 
часы, минуты, секунды, задающие первый момент времени 
и три целых числа, задающих второй момент времени.

Выведите число секунд между этими моментами времени.

"""
h1 = int(input("input h1:"))
m1 = int(input("input m1:"))
s1 = int(input("input s1:"))

h2 = int(input("input h2:"))
m2 = int(input("input m2:"))
s2 = int(input("input s2:"))

t1 = h1*60*60+m1*60+s1
t2 = h2*60*60+m2*60+s2
ds = t2-t1
print(ds)
