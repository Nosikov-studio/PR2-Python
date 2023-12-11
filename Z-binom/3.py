a = 2448
print(bin(a))
s = 1
print(s << 2)  # 1 перейдет в 100 в двоичной системе или 4 в десятичной
print(bin(s << 2))
print(a*(s << 2))  # умножение 2448 на 4
print(a & (s << 2))
print(a & (s << 3))
print(a & (s << 4))
print(a & (s << 5))
print(a & (s << 6))
print(a & (s << 7))

n = 0
for i in range(len(bin(a))-2):
    if a & (s << i) > 0:
        n += 1
print(n)
