"""
Задача «Номер появления слова»
Условие
В единственной строке записан текст. 
Для каждого слова из данного текста подсчитайте, 
сколько раз оно встречалось в этом тексте ранее.

Словом считается последовательность непробельных 
символов идущих подряд, 
слова разделены одним или большим числом пробелов 
или символами конца строки.

"""
s = []
F = []
s = input().split()
# print(s)
for i in range(len(s)):
    f = 0
    for j in range(i):
        if s[i] == s[j]:
            f += 1
    F.append(str(f))
# print(s)
# print(F)
s2 = ""
s2 = " ".join(F)
print(s2)
