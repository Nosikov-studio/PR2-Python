a = 2448
b = bin(a)
print(b)
print(len(b))
s = 1
s1 = s << 2
print(s1)
print(bin(s1))

for i in range(len(bin(a))-2):
    print(bin(s << i))
    # print(b & bin(s << i))
print("******************")
print(a*(s << i))
