# декоратор
def createAddress(func):
    tp = 'Гражданин '

    def w():
        address = tp.upper()
        name = func()
        s = f'{address}{name}'
        return s
    return w


@createAddress
def addresGrajdanin():
    return 'Василий'


print(addresGrajdanin())
