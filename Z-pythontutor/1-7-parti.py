"""
Задача «Парты»
Условие
В школе решили набрать три новых математических класса. 
Так как занятия по математике у них проходят в одно и то же время, 
было решено выделить кабинет для каждого класса 
и купить в них новые парты. 
За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов. 
Сколько всего нужно закупить парт чтобы их хватило на всех учеников? 
Программа получает на вход три натуральных числа: 
количество учащихся в каждом из трех классов.
Во всех задачах считывайте входные данные через input() 
и выводите ответ через print().

"""
import math
n1 = int(input("input first numper:"))
n2 = int(input("input second numper:"))
n3 = int(input("input third numper:"))
p1 = math.ceil(n1/2)
p2 = math.ceil(n2/2)
p3 = math.ceil(n3/2)
p = p1+p2+p3
print(p)
