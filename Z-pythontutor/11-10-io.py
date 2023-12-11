"""
https://education.yandex.ru/handbook/python/article/potokovyj-vvodvyvod-rabota-s-tekstovymi-fajlami-json
Потоковый ввод/вывод.
Как обрабатывать данные, 
не имея понятия о их количестве?
ЗАДАЧА A+B+...

Завершаем поток ввода в Windows:
1) Ctrl + Z (появится ^Z)
2) Жмем enter
"""
from sys import stdin

#1
s=0
for line in stdin:
    s+=sum(map(int, line.split()))
print(s)
#2
lines = []
for line in stdin:
    lines.append(line)
print(lines)
