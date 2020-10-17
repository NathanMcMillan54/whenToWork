from tkinter import *
import time
import os

root = Tk()
root.title("whenToWork")

TT = Label(root, text="whenToWork")
TT.config(font=("Courier", 14))
TT.pack()


def inputText(projectValue):
    # python can increase a value about 55000 times
    # in a second in a while loop
    i = 0

    if projectValue > 6:
        print("Work for 60 minutes")
        while True:
            i += 1
            if 1 == 198000000:
                os.system('python whenToWork/stop.py')
                print("Stop")
                exit()

    elif projectValue < 4:
        print("Work for 15 minutes")
        while True:
            i += 1
            if 1 == 49500000:
                os.system('python whenToWork/stop.py')
                print("Stop")
                exit()
    elif projectValue == 4:
        print("Work for 30 minutes")
        while True:
            i += 1
            if 1 == 99000000:
                os.system('python whenToWork/stop.py')
                print("Stop")
                exit()
    elif projectValue == 5:
        print("Work for 45 minutes")
        while True:
            i += 1
            if 1 == 148500000:
                os.system('python whenToWork/stop.py')
                print("Stop")
                exit()
    elif projectValue == 6:
        print("Work for 45 minutes")
        while True:
            i += 1
            if 1 == 148500000:
                os.system('python whenToWork/stop.py')
                print("Stop")
                exit()


def enter():
    print("Entered all values")
    project = inputProjectBox.get("1.0", "end-1c")
    print(project)
    projectValue = int(inputProjectValueBox.get("1.0", "end-1c"))
    print(projectValue)
    inputText(projectValue)


PT = Label(root, text="Project Name")
PT.config(font=("Courier", 14))
PT.pack()

inputProjectBox = Text(root, height=2, width=10)
inputProjectBox.pack()

PVT = Label(root, text="Input 1-10")
PVT.config(font=("Courier", 14))
PVT.pack()

inputProjectValueBox = Text(root, height=2, width=10)
inputProjectValueBox.pack()

enterButton = Button(root, height=1, width=10, text="Enter", command=lambda: enter())
enterButton.pack()

root.geometry("500x500")
root.mainloop()
