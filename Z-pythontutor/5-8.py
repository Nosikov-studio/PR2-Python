"""
Задача «Обращение фрагмента»
Условие
Дана строка, в которой буква h встречается как минимум два раза. 
Разверните последовательность символов, 
заключенную между первым и последним появлением буквы h, 
в противоположном порядке.
"""
s = input("Input a string:")
n1 = s.find("h")
n2 = s.rfind("h")
si = s[n1:(n2+1)]
si2 = si[::-1]
ls = s[:n1]
rs = s[n2+1:]
news = ls+si2+rs
print(news)
