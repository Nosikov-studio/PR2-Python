my_str1 = 'blabla'
name = 'vasia pupkin'

print(name.title())
print(name.upper())
print(name.lower())
print("stroka1\nstroka2\n\nstroka3")
print("message1\n\tmessage2\n\tmessage3")

a = "  . .  ,  deda vasya . . . "
print(a)
print(a.rstrip())
print(a.lstrip())

print(a.strip(",. "))
print("************split***********************")
s1 = "gorelukovoe moe takoe"
list1 = s1.split()
list2 = s1.split('o')
print(list1)
print(list2)
print("==============join=======================")

s2 = '+'.join(s1)
print(s2)
print("///////////////////join///////////////////")
list2 = ['8', 'a', 'bla', 'bla', "80"]
s3 = "+".join(list2)
print(s3)

print("@@@@@@@@@@@@@@@@@@@join@@@@@@@@@@@@@@@@@@@")
list4 = [8, 913, 403, 88, 80]
s4 = "-".join(map(str, list4))
print(s4)
print("&&&&&&&&&&&&&&&&map&&&&&&&&&&&&&&&&&&&&&&&&&&")
list5 = [1, 2, 3, 4, 5]
x1 = map(lambda x: x * 10, list5)
print(x1)
print(list5)
x2 = list(map(lambda x: x * 20, list5))
print(x2)
