# Прямой отсчет
N1 = 8
sp = ""
so = ""


def rcp(N):
    global sp
    if N == 0:
        sp = sp + '0'
    else:
        rcp(N-1)  # Последовательность операций!!!!!!!!
        sp = sp + ' '+str(N)

    return sp


print(rcp(N1))


# Обратный отсчет
N2 = 23


def rco(N):
    global so
    if N == 0:
        so = so+' 0'
    else:

        so = so+' '+str(N)
        rco(N-1)
    return so


print(rco(N2))
