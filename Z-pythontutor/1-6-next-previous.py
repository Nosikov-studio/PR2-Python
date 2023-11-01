"""
Задача «Следующее и предыдущее»
Условие
Напишите программу, которая считывает целое число и выводит текст, 
аналогичный приведенному в примере (пробелы важны!).
Во всех задачах считывайте входные данные через input() 
и выводите ответ через print().
***
input:1534
The next number for the number 1534 is 1535.
The previous number for the number 1534 is 1533.
"""
s = input("Input number:")
n = int(s)
nn = n+1
pn = n-1
snn = "The next number for the number "+str(n)+" is "+str(nn)+"."
spn = "The previous number for the number "+str(n)+" is "+str(pn)+"."
print(snn)
print(spn)
