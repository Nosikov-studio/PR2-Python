# решение разработчиков
def reverse():
    x = int(input()) # значение не затирается, т.к работает уже другая функция!!!
    
    if x != 0:
        reverse()
    print(x)


reverse()
