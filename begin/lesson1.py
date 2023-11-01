# РАЗМИНКА №1
nums = [2,7,11,15]
m=[]
sum=0 
target = 9
for i in nums:
    sum+=i
    m.append(i+1)
    print(i)
#выводим новый массив с суммой в конце    
m.append(sum)
print(m)
print("*********************************")
# длина списка (массива)
n=len(nums)
print("n=", n)


