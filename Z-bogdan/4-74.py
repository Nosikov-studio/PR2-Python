s1 = {35, 69, 84}
s1.add(33)
print(s1)
s2 = {69, 84, 101, 108}

s3 = s1.intersection(s2)

li = list(s3)
print(li)

s4 = s1 | s2
print(s4)
li4 = list(s4)
li4.sort()
print(li4)
