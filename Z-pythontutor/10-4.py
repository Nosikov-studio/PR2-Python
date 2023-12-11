"""
Задача «Встречалось ли число раньше»
Условие
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO, 
если не встречалось.

"""
s1 = []
s2 = set()
s3 = []
for i in input().split():
    s1.append(int(i))
    if int(i) in s2:
        s3.append('YES')
        print('YES')
    else:
        s3.append('NO')
        print('NO')
    s2.add(int(i))


# print(s1)
# print(s2)
# print(s3)
