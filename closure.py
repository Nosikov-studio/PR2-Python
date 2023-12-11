# замыкание
def createAddress(tp):
    address = tp.upper()

    def w(name):
        s = f'{address}{name}'
        return s
    return w


addresGrajdanin = createAddress('Гражданин ')
addresGrajdanka = createAddress('Гражданка ')

print(addresGrajdanin('Василий'))
print(addresGrajdanin('Алёна'))
