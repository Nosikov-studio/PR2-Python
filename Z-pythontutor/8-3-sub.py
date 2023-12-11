s = input("vvedite stroku:")

s1 = s
s2 = s1.split()
s3 = s2
for i in range(len(s2)):
    s3[i] = list(s2[i])
# Как разбить цельное слова в список? Предложение умеем разбивать по пробелам.

print(s3)
