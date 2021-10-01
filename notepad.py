from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# newfile code


def Newfile():
    global file
    root.title("Untitled-Notepad")
    file = None
    textarea.delete(1.0, END)
# openfile code


def Openfile():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[
                             ("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

# savefile code


def Savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("File Saved")

    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

# exitfile code


def Exitfile():
    root.destroy()
# cut code


def cut():
    textarea.event_generate(("<<Cut>>"))

# copy code


def copy():
    textarea.event_generate(("<<Copy>>"))
# paste code


def paste():
    textarea.event_generate(("<<Paste>>"))

# about code


def about():
    showinfo("Notepad", "Notepad by MOHAMMAD SAQIB")


root = Tk()
root.title("Untitled-Notepad")
root.geometry("500x300")
# Add textarea
textarea = Text(root, font="lucida 13")
file = None
textarea.pack(expand=True, fill=BOTH)

# create a menubar
menubar = Menu(root)

# filemenu
filemenu = Menu(menubar, tearoff=0)
# to open a new file
filemenu.add_command(label="New", command=Newfile)
# to open already existing  file
filemenu.add_command(label="Open", command=Openfile)
# to save the current file
filemenu.add_command(label="Save", command=Savefile)
# for seperate
filemenu.add_separator()
# to exit
filemenu.add_command(label="Exit", command=Exitfile)
menubar.add_cascade(label="File", menu=filemenu)


# eidt menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=editmenu)

# helps menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About Notepad", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# adding a scrollbar
scrl = Scrollbar(textarea)
scrl.pack(side=RIGHT, fill=Y)
scrl.config(command=textarea.yview)
textarea.config(yscrollcommand=scrl.set)


# pack mainloop
root.mainloop()
