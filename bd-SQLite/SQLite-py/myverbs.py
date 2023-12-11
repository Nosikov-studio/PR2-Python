import sqlite3 as sq
import random
from tkinter import *
import tkinter.messagebox as mb


def f1():
    x = random.randint(1, 5)
    with sq.connect("verb.db") as con:
        cur = con.cursor()
        cur.execute("SELECT verb_en FROM verbs WHERE verb_id= :x1", {'x1': x})
        result = cur.fetchone()
        print(result[0])
        print(x)
    return result[0]


def f2():
    verb = f1()
    l["text"] = verb
    return verb


def f3():
    verb = f1()
    mb.showinfo(title='soobsh', message=verb)
    return verb


root = Tk()
root.title("Enlish Verb")
root.geometry("400x600")
root.resizable(width="False", height="False")

v = StringVar()


l = Label(text="", bg="yellow", fg="brown",
          font=('Arial', 30, 'bold'), padx='20', pady='40')
b = Button(text="Получить глагол!", command=f2)
b2 = Button(text="b2 кнопка", command=f3)

# b.bind('< Button-1 >', f2)  # ?????????????
b.pack()
l.pack()
b2.pack(side=BOTTOM, pady=40)

root.mainloop()
