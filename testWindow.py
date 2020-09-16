from tkinter import *

root = Tk()
root.title("whenToWork")
root.configure(background="#ffffff")

L = Label(root, text="whenToWork")
L.config(font=("Courier", 14))
L.pack()


# add stuff to make input

def getInput():
    project = inputBox.get("1.0", "end-1c")
    print(project)


inputBox = Text(root, height=2, width=10)
inputBox.pack()
buttonCommit = Button(root, height=1, width=10, text="Enter", command=lambda: getInput())

buttonCommit.pack()

root.geometry("500x500")
root.mainloop()
