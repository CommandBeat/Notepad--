from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import simpledialog
import os
import pyperclip

os.chdir(r"C:\Users\Admin\Desktop\code\python")

root = Tk()
root.title("Notepad--")

currentFile = None
lastFound = None
t = Text(root, height=5, width=52)
t.pack()


def openFile():
    filetypes = (
        ("text files", "*.txt"),
        ("All files", "*.*")
    )
    file = fd.askopenfile(filetypes=filetypes)
    with open(os.path.basename(file.name), "r") as f:
        t.delete("1.0", END)
        t.insert(END, f.read())


def newFile(name="newFile"):
    with open(name+".txt", "w") as f:
        f.write(t.get("1.0", END))
        global currentFile
        currentFile = "newFile.txt"


def saveFile():
    if currentFile != None:
        with open(currentFile, "w") as f:
            f.write(t.get("1.0", END))
    elif currentFile == None:
        newFile(None)


def saveAs():
    fileName = simpledialog.askstring("File Name", "What will you name your file?")
    if fileName:
        if currentFile == None:
            newFile(fileName)
        else:
            try:
                os.rename(currentFile, fileName)
            except Exception:
                newFile(fileName)
            


menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu = file)
file.add_command(label="New File", command=newFile)
file.add_command(label="Open...", command=openFile)
file.add_command(label="Save", command=saveFile)
file.add_command(label="Save as...", command=saveAs)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)


def copy():
    pyperclip.copy(t.get("1.0", END))


def paste():
    t.insert(END, pyperclip.paste())


def find():
    txt = simpledialog.askstring("Find", "What do you want to find?")
    if txt:
        text = t.get("1.0", END)
        if txt in text:
            print("Found it!")
            global lastFound
            lastFound = txt


def findAgain():
    if lastFound != None:
        text = t.get("1.0", END)
        if lastFound in text:
            print("Found it again!")


edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=None)
edit.add_command(label="Copy", command=copy)
edit.add_command(label="Paste", command=paste)
edit.add_separator()
edit.add_command(label="Find...", command=find)
edit.add_command(label="Find again", command=findAgain)

help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_)
help_.add_command(label="Tk Help", command=None)
help_.add_command(label="Demo", command=None)
help_.add_separator()
help_.add_command(label="About Tk", command=None)

root.config(menu=menubar)
mainloop()