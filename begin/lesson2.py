# bame=input("vvedite:")
# print("hello world", bame)

m1 = [5, 99, 2, -66, 36, 48, 1, 888, 99, 124, 2, 44, 59]
m2 = [1, 2, 3]

# 1) Подсчёт элементов
# count = 0
# for i in m1:
#     count += 1
# print(count)

# 2) Определение суммы элементов
# sum = 0
# for i in m1:
#     sum += i
# print(sum)

# 3) Определение максимального элемента
# maxim = m1[0]
# for i in m1:
#     if i > maxim:
#         maxim = i
# print(maxim)
# print("по индексу:", m1.index(maxim)) #русский язык???

# 4) То же самое, только с оформлением функции


# def maxim(A):
#     maxi = A[0]
#     for i in A:
#         if i > maxi:
#             maxi = i
#     return maxi


# print(maxim(m1))


# 5) Поиск минимума
# def minim(A):
#     mini = A[0]
#     for i in A:
#         if i < mini:
#             mini = i
#     return mini


# print(minim(m1))

# 6) Поиск числа
# def search(x, A):
#     ind = -1
#     for i in A:
#         if x == i:
#             ind = A.index(i)
#     return ind


# print(search(48, m1))

# 7) Найти первых два максимума

def maxtwo(A):
    max1 = A[0]
    max2 = A[1]
    for i in A:
        if i > max1:
            max1 = i
    for i in A:
        if ((i > max2) and (i != max1)):
            max2 = i
    M = (max1, max2)
    return M


print(maxtwo(m2))
