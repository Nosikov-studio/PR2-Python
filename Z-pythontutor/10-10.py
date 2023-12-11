"""
Задача «Забастовки»
Условие
Политическая жизнь одной страны очень оживленная.
 В стране действует K политических партий, 
 каждая из которых регулярно объявляет национальную забастовку.
  Дни, когда хотя бы одна из партий объявляет забастовку, 
  при условии, что это не суббота или воскресенье 
  (когда и так никто не работает), 
  наносят большой ущерб экономике страны.


i-я партия объявляет забастовки строго каждые b_i дней, 
начиная с дня с номером a_i. То есть i-я партия объявляет 
забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д. 
Если в какой-то день несколько партий объявляет забастовку,
 то это считается одной общенациональной забастовкой.

В календаре страны N дней, пронумерованных, начиная с единицы. 
Первый день года является понедельником, 
шестой и седьмой дни года — выходные, 
неделя состоит из семи дней.

В первой строке даны числа N и K. 
Далее идет K строк, описывающие графики проведения забастовок.
 i-я строка содержит числа a_i и b_i. 
 Вам нужно определить число забастовок, 
 произошедших в этой стране в течении года.
"""


n, k = [int(i) for i in input().split()]


z = set()

for i in range(k):
    a_i, b_i = [int(i) for i in input().split()]

    j = 0
    while a_i+j*b_i <= n:
        if ((a_i+j*b_i) % 7 != 0) or ((a_i+j*b_i+1) % 7 != 0):
            z.add(a_i+j*b_i)
        if ((a_i+j*b_i) % 7 == 0) or ((a_i+j*b_i+1) % 7 == 0):
            z.discard(a_i+j*b_i)
        j += 1
# print(z)
print(len(z))
