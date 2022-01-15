import tkinter.ttk
import tkinter

myWin = tkinter.Tk()
myStringVar = tkinter.StringVar()

myList = []


myBox = tkinter.ttk.Combobox(master=myWin, textvariable=myStringVar, values=myList)


myList = ["Tim", "jame", "tame"]

myBox.configure(values=myList)
myBox.pack()

myWin.mainloop()