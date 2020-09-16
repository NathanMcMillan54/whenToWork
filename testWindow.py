from tkinter import *
import time
import os

root = Tk()
root.title("whenToWork")

TT = Label(root, text="whenToWork")
TT.config(font=("Courier", 14))
TT.pack()


def inputText():
    # get input from both input boxes
    projectValue = int(1)

    if projectValue > 7:
        print("Work for 60 minutes")
        time.sleep(3600)
        os.system('python whenToWork/stop.py')
        print("Stop")
        exit()
    elif projectValue < 3:
        print("Work for 15 minutes")
        time.sleep(900)
        os.system('python whenToWork/stop.py')
        print("Stop")
        exit()
    elif projectValue == 4:
        print("Work for 30 minutes")
        time.sleep(1800)
        os.system('python whenToWork/stop.py')
        exit()
    elif projectValue == 5:
        print("Work for 45 minutes")
        time.sleep(2700)
        os.system('python whenToWork/stop.py')
        exit()
    elif projectValue == 6:
        print("Work for 45 minutes")
        time.sleep(2700)
        os.system('python whenToWork/stop.py')
        exit()


def getProjectInput():
    project = inputProjectBox.get("1.0", "end-1c")
    print(project)
    inputText()


def getProjectValueInput():
    projectValue = int(inputProjectValueBox.get("1.0", "end-1c"))
    print(projectValue)
    inputText()


PT = Label(root, text="Project Name")
PT.config(font=("Courier", 14))
PT.pack()

inputProjectBox = Text(root, height=2, width=10)
inputProjectBox.pack()
# soon figure out how to only have 1 input button and 2 input boxes
buttonEnterProject = Button(root, height=1, width=10, text="Enter", command=lambda: getProjectInput())
buttonEnterProject.pack()

PVT = Label(root, text="Input 1-10")
PVT.config(font=("Courier", 14))
PVT.pack()

inputProjectValueBox = Text(root, height=2, width=10)
inputProjectValueBox.pack()
buttonEnterProjectValue = Button(root, height=1, width=10, text="Enter", command=lambda: getProjectValueInput())

buttonEnterProjectValue.pack()

root.geometry("500x500")
root.mainloop()
