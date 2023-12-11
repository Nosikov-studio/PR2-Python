# Прямой отсчет
N1 = 8


def rcp(N):

    if N == 0:
        print(0)
    else:
        rcp(N-1)  # Последовательность операций!!!!!!!!
        print(N)

    return ""


print(rcp(N1))


# Обратный отсчет
N2 = 23


def rco(N):

    if N == 0:
        print(0)
    else:

        print(N)
        rco(N-1)
    return ""


print(rco(N2))
