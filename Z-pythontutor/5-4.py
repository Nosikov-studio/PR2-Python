"""
Задача «Переставить два слова»
Условие
Дана строка, состоящая ровно из двух слов, разделенных пробелом. 
Переставьте эти слова местами. 
Результат запишите в строку и выведите получившуюся строку.

При решении этой задачи не стоит пользоваться циклами и инструкцией if.

"""

s = input("Input a string:")
r = s.find(" ")
w1 = s[:r]
w2 = s[r+1:]
news = w2+" "+w1
print(news)
