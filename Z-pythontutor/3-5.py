"""
Задача «Конец уроков»
Условие
В некоторой школе занятия начинаются в 9:00. 
Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. 
уроков перемена 5 минут, 
а после 2-го, 4-го, 6-го и т.д. — 15 минут.

Дан номер урока (число от 1 до 10). 
Определите, когда заканчивается указанный урок.

Выведите два целых числа: время окончания урока в часах и минутах.


"""
n = int(input("input n:"))
L = n*45+5*int(n/2)+15*int((n-1)/2)
H1 = L//60
H = 9+H1
M = L % 60
print(H, M)
