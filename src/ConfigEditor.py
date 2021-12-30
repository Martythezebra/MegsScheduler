import tkinter
import CastMember


class ConfigEditor:
    def __init__(self):
        self.topLevelWindow = tkinter.Tk()
        self.castMemberBoxList = {}
        self.castMemberFrame = tkinter.Frame()
        self.myTopBar = TopBar()
        self.ROW_LENGTH = 3

    # generate a new CastMemberBox around a CastMember and add it to the display
    def addCastMember(self, castmemberArg):
        
        window = CastMemberBox(castmemberArg, self)                       # pass cast member to be wrapped in tkinter window element

        self.castMemberBoxList[castmemberArg.getName()] = window    # add returned cast member window to topLevelWindow's array

    def begin(self):
        self.myTopBar.createButtons()
        self.castMemberFrame.grid(row=1)
        # TODO: pack in "save/file/edit" bar at row = 0, right above the grid of cast members
        entryNumber = 0
        for member in self.castMemberBoxList:
            currentMember = self.castMemberBoxList[member]
            currentMember.createLabel(self.castMemberFrame)
            self.castMemberBoxList[member].castMemberBoxWindow.grid(column=entryNumber % self.ROW_LENGTH, row = entryNumber // self.ROW_LENGTH)
            entryNumber += 1

        self.topLevelWindow.mainloop()

class TopBar:
    def __init__(self):
        self.bar = tkinter.Frame()
    
    def createButtons(self):
        self.savebutton = tkinter.Button(master=self.bar, text="Save All", )
        self.savebutton.bind("<ButtonRelease-1>", TopBar.saveButtonClicked)
        self.savebutton.grid(row=0, column=0)

        self.filebutton = tkinter.Button(master=self.bar, text="File (placeholder)")
        self.filebutton.bind("<ButtonRelease-1>", TopBar.fileButtonClicked)
        self.filebutton.grid(row=0, column=1)

        self.bar.grid(row=0)

    def saveButtonClicked(event):
        print("yeetus")

    def fileButtonClicked(event):
        print("yimpus")



class CastMemberBox:
    def __init__(self, castMemberArg, parent):
        self.myCastMember = castMemberArg
        self.myRoles = castMemberArg.createRoleDictionary()
        self.myCheckboxes = CheckboxBlock(self)
        self.myParent = parent

    def createLabel(self, topLevel):
        self.castMemberBoxWindow = tkinter.Frame(master=topLevel, relief=tkinter.RAISED, borderwidth=2)
        self.nameWindow = tkinter.Label(master=self.castMemberBoxWindow, text=self.myCastMember.getName(), relief=tkinter.SUNKEN, borderwidth=2)
        self.nameWindow.grid(row=0, column=0)
        self.myCheckboxes.createRows(self.castMemberBoxWindow, self.myRoles)

class CheckboxBlock:
    def __init__(self, parent):
        self.checkboxList = {}
        self.isCheckedList = {}
        self.myParent = parent

    def createRows(self, topLevel, roleDictionary):
        for roleName in roleDictionary:
            self.isCheckedList[roleName] = tkinter.BooleanVar(master=topLevel, name=self.myParent.myCastMember.name + "_" + roleName, value=roleDictionary[roleName])
            self.checkboxList[roleName] = tkinter.Checkbutton(master=topLevel, text=roleName, variable=self.isCheckedList[roleName])
            self.checkboxList[roleName].grid()

