# 1
d = {}
# 2
for i in range(3):
    k = input("key:")
    v = input("value:")
    d[k] = v

print(d)

d['name'] = "Lola"
print(d)
del d['2']
print(d)
