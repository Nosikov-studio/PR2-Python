'''
Дана строка (в кодировке UTF-8). 
Найти самый часто встречаемый в ней символ. 
Если несколько символов встречаются одинако часто,
то можно вывести любой.

'''

stroka = 'abracadabra'
m=list(stroka)
print('**********************************')
n=len(m)
print(n)
m1=[]

for i in m:
    ind=m.index(i)
    m1.append(ind)

print(m1)
mi=[]
ms=[0]*n
print(ms)

indexm1=0

for i in m1:
    #print(indexm1)
    #print(i)
    indexm1+=1
    for j in range(indexm1,n):
        if i==m1[j]:
            ms[j]+=1
    
    #print('*****')

print(m1)
print(ms)
max_number = max(ms)
print(max_number)
indexmax=ms.index(max_number)
print(indexmax)
print(m[indexmax])