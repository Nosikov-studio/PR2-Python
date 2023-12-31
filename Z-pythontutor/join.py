# список чисел --> список строк --> одна строка
# 1 способ (список чисел --> список строк)
# через генератор списка

an1 = [35, 75, 69, 55, 1, 15, 108, 9]

ast1 = [str(i) for i in an1]  # <-- через генератор списка
s = " ".join(ast1)
print(s)

# 2 способ (список чисел --> список строк)
# через map

an2 = [333, 75, 69, 55, 1, 15, 108, 999]
ast2 = list(map(str, an2))
s = " ".join(ast2)
print(s)
