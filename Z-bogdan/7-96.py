

def u(**car):
    car['is_available'] = True
    return car


d2 = u(bd="volvo", pr=5500)
print(d2)
