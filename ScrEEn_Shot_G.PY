from tkinter import *
from PIL import ImageGrab
import time

window = Tk()

window.title("scrin shot")


def scrin ():
    time.sleep(3)
    sc = ImageGrab.grab()
    sc.save(name.get()+'.'+family_name.get())


window.minsize(350,150)
window.maxsize(600,150)

Label(window, text="scrin shot name").pack()


name = Entry(window)
name.pack()


Label(window, text="format scrin shot").pack()


family_name = Entry(window)
family_name.pack()


btn = Button(window,text="scrin shot run",command=scrin)
btn.pack()


user_name = Label(window)
user_name.pack()


window.mainloop()

