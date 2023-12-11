# a = {6, 7, 8, 9, 10}
# b = {2, 4, 6, 8, 10}

# z = a-b
# print(z)
# print(a - (a & b))

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

a = input('input series:')
ams = a.split()
amn = [int(i) for i in ams]
amns = set(amn)
print(s)
print(amns)
print(s & amns)
