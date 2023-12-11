"""
Подсчитать количество единиц в двоичной записи числа
"""

b = 0b0000100110010000
print(int(b))
print(type(b))

s = str(b)
M = s.split()
print(M)

b2 = '0000100110010000'
M = b2.split()
print(M)

b3 = list(b2)
print(b3)

b4 = [int(i) for i in b3]
print(b4)
sum = 0
for i in b4:
    sum += i
print(sum)

print("*****************************")
a = 2**11+2**8+2**7+2**4
print(a)
print(bin(a))
# инвертирование
print(bin(~a))
#
f = 5
m = 4
r = 5 & 4
print(r)
print(bin(f))
print(bin(m))
print(bin(r))
#
print(bin(a))
print(bin(a >> 1))
print(bin(a))
print(bin(a << 1))
