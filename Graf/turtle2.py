import turtle

# tracer(f, [delay]) – отображение процесса рисования.
# По умолчанию визуализация включена.
# Если f = 1, то процесс рисования отображается (значение по умолчанию).
# Если f = 0, то процесс рисования не отображается.
# Второй параметр в миллисекундах (задержка между шагами)
# turtle.tracer(1, 100)

turtle.speed(10)

turtle.bgcolor('black')
# bgcolor('цвет') – установка цвета фона окна для рисования.
# По умолчанию цвет фона белый


turtle.shape('turtle')
turtle.color('pink')
turtle.width(10)  # установить толщину пера 10px


# up() – поднять перо.
# down() – опустить перо.

turtle.down()
turtle.forward(150)
turtle.goto(100, 75)

# forward(шаг) – перемещение вперед. fd() - алиас (сокращение).
# backward(шаг) – перемещение назад.
# goto(x, y) – перемещение пера в точку с координатами (x,y).
# (0,0) - начальное положение черепашки (где-то в середине экрана)
turtle.left(90)
turtle.forward(100)

# right(угол) – поворот вправо.
# left(угол) – поворот влево.
turtle.left(90)
turtle.up()
turtle.forward(150)
turtle.down()
turtle.dot(20, 'white')

# dot([size],[color]) – рисует точку в текущей позиции Черепахи
turtle.width(1)
turtle.circle(50)
turtle.color('green')
turtle.circle(20)

turtle.color('blue', 'yellow')
turtle.forward(150)
turtle.width(7)
turtle.begin_fill()
turtle.circle(-30)
turtle.end_fill()
turtle.circle(30)
turtle.forward(80)
turtle.write('Python', font=("Arial", 20, "normal"))

# write(строка) – вывод текста.
# turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))

turtle.left(90)
turtle.forward(80)
turtle.write(turtle.window_width())
turtle.goto(50, 50)
turtle.write(turtle.position(), font=("Arial", 20, "normal"))

# window_width() – получает текущую ширину окна.
# window_height() – получает текущую высоту окна.
# position() – получает текущую позицию Черепахи.

# turtle.xcor() – получает координату x текущей позиции Черепахи.
# turtle.ycor() – получает координату y текущей позиции Черепахи.
# turtle.setx(число) – изменение координаты x Черепахи
# turtle.sety(число) – изменение координаты y Черепахи.

turtle.setx(20)
turtle.sety(20)
turtle.write(turtle.position())

pen1 = turtle.Turtle()
pen1.pencolor('red')
# pencolor(цвет) – цвет пера.
# fillcolor(цвет) – цвет заливки.
pen1.width(5)
pen1.down()
pen1.backward(200)
pen1.right(90)
pen1.forward(150)
pen1.left(90)
pen1.fd(150)
pen1.circle(50)

pen1.color('#33cc8c')
pen1.fd(100)
pen1.circle(-50)

pen1.color('#130081')
pen1.fd(130)
pen1.circle(80, 90)
pen1.fd(230)
# circle(r, a) – рисование дуги.
pen1.begin_fill()
pen1.circle(-30)
pen1.end_fill()
pen1.circle(30)
pen1.fd(100)
pen1.left(90)
pen1.fd(300)

# begin_fill() – включение закрашивания области.
# end_fill() – выключение закрашивания области.

# turtle.done()
# turtle.getscreen()._root.mainloop()
# turtle.Screen().mainloop()
turtle.mainloop()
# mainloop() – задержка окна.
