"""
Задача «Дробная часть»
Условие
Дано положительное действительное число X. 
Выведите его дробную часть.

"""
import math
X = float(input("input X:"))
XZ = math.floor(X)
XD = X-XZ
print(XD)

"""
ДРУГОЕ РЕШЕНИЕ 2
X = float(input("input X:"))
print(X - int(X))
ДРУГОЕ РЕШЕНИЕ 3
X = float(input("input X:"))
print(X%1)

"""
