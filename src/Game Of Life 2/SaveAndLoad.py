import tkinter

class SaveAndLoad:

    def __init__(self):
        print("inside init")

    def prepareWindow(self,event):
        self.window = tkinter.Toplevel()
        self.fileNameEntry = tkinter.Entry(master=self.window)
        self.window.bind("<q>",self.quit)
        self.window.mainloop()


    def quit(self):
        self.window.destroy()