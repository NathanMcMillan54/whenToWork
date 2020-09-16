from tkinter import *

root = Tk()
root.title("whenToWork")

TT = Label(root, text="whenToWork")
TT.config(font=("Courier", 14))
TT.pack()


# add stuff to make input

def getProjectInput():
    project = inputProjectBox.get("1.0", "end-1c")
    print(project)


def getProjectValueInput():
    projectValue = inputProjectValueBox.get("1.0", "end-1c")
    print(projectValue)


PT = Label(root, text="Project Name")
PT.config(font=("Courier", 14))
PT.pack()

inputProjectBox = Text(root, height=2, width=10)
inputProjectBox.pack()
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
