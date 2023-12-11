# "Вводим строку. Переворачиваем строку, используя рекурсию"

# s1 = "aberval"
# s2 = ""
ms = input("stroka")


def foo(stroka):
    s1 = stroka
    N1 = len(s1)-1
    global s2
    s2 = ""

    def rcp(N):
        global s2
        if N == 0:
            s2 = s2+s1[0]
        else:
            s2 = s2+s1[N]
            rcp(N-1)

        return s2
    return rcp(N1)


print(foo(ms))
