import turtle

t = turtle.Pen()
turtle.bgcolor('black')

for x in range(30):
    t.pencolor('red')
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
t.clear()
turtle.reset()


turtle.shape('turtle')
turtle.down()
turtle.color('orange')
turtle.width(10)
turtle.circle(50)
turtle.circle(-50)

turtle.clear()

pen1 = turtle.Turtle()
pen2 = turtle.Turtle()

pen1.pencolor('red')
pen2.pencolor('green')

pen1.up()

pen1.goto(0, -22)
pen1.down()
pen1.left(100)
pen1.fd(150)
# рисунок пера pen2
pen2.up()
pen2.goto(0, 22)
pen2.down()
pen2.right(100)
pen2.fd(150)
# очищаем рисунок пера pen1
# pen1.clear()

turtle.done()
