x = 0
y = 0
s = ''
while True:

    if y < 15:
        if x == 10:
            x = 0
            s = ''
            y += 1
        s += str(x)
        print('row', y, 'plase:', s)

        x += 1
    else:
        y = 0
