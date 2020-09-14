from tkinter import *
import os

root = Tk()
root.title("Stop working")
root.configure(background='#ffffff')

L = Label(root, text="Stop Working! Take a break")
L.config(font=("Courier", 14))
L.pack()


def closeWin():
    exit()


Btn = Button(root, text="Ok", command=closeWin, fg='#000000')
Btn.pack()


def beep():
    os.system('sh beep.sh')


beep()

root.mainloop()
