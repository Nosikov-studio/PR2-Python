from tkinter import *

root = Tk()

root.title("Lesson")
root.geometry("400x200+300+300")
root.resizable(width=False, height=False)
root.config(bg="green")
v = StringVar()

l = Label(text="Текстовый текст")
e = Entry(textvariable=v)
b = Button(text="Ok")


def test1(event):
    v1 = v.get()
    l['text'] = v1
    print("Всё работает!!!")


b.bind('<Button-1>', test1)


# grid(), pack(), place()
l.grid(row=1, column=1)
e.grid(row=2, column=1)
b.grid(row=3, column=1)


root.mainloop()
