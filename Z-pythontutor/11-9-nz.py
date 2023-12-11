# функция, которая считает количество заглавных букв в слове
def nz(word):
    counter = 0
    for ch in word:
        if ch.isupper():
            counter += 1
    return counter


print(nz('lower'))
