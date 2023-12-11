# замыкание
def createAddress(tp):

    def w(name):
        address = tp.upper()
        s = f'{address}{name}'
        return s
    return w


addresGrajdanin = createAddress('Гражданин ')

print(addresGrajdanin('Василий'))
