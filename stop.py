from tkinter import *
import os

root = Tk()
root.title("Stop working")
root.configure(background='#ffffff')

L = Label(root, text="Stop Working! Take a break")
L.config(font=("Courier", 14))
L.pack()


def beep():
    os.system('sh beep.sh')


beep()

root.mainloop()
