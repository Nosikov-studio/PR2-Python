"""
https://www.youtube.com/watch?v=z50Xjwkfh7Q
"""


import turtle

t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x/100+1)  # линия делается толще
    t.fd(x)
    t.rt(59)

t.clear()
turtle.reset()
