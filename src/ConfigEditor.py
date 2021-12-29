import tkinter
import CastMember


class ConfigEditor:
    def __init__(self):
        self.topLevelWindow = tkinter.Tk()
        self.castMemberBoxList = {}
        self.castMemberFrame = tkinter.Frame()
        self.ROW_LENGTH = 3

    # generate a new CastMemberBox around a CastMember and add it to the display
    def addCastMember(self, castmemberArg):
        
        window = CastMemberBox(castmemberArg)                       # pass cast member to be wrapped in tkinter window element

        self.castMemberBoxList[castmemberArg.getName()] = window    # add returned cast member window to topLevelWindow's array

    def begin(self):
        self.castMemberFrame.grid(row=1)
        # TODO: pack in "save/file/edit" bar at row = 0, right above the grid of cast members
        entryNumber = 0
        for member in self.castMemberBoxList:
            currentMember = self.castMemberBoxList[member]
            currentMember.createLabel(self.castMemberFrame)
            self.castMemberBoxList[member].castMemberBoxWindow.grid(column=entryNumber % self.ROW_LENGTH, row = entryNumber // self.ROW_LENGTH)
            entryNumber += 1

        self.topLevelWindow.mainloop()




class CastMemberBox:
    def __init__(self, castMemberArg):
        self.myCastMember = castMemberArg
        self.myRoles = castMemberArg.createRoleDictionary()
        self.myCheckboxes = CheckboxBlock()

    def createLabel(self, topLevel): # Takes in the parent frame as an argument
        self.castMemberBoxWindow = tkinter.Frame(master=topLevel, relief=tkinter.RAISED, borderwidth=1)
        self.nameWindow = tkinter.Label(master=self.castMemberBoxWindow, text=self.myCastMember.getName())
        self.nameWindow.grid(row=0, column=0)
        self.myCheckboxes.createRows(self.castMemberBoxWindow, self.myRoles)

class CheckboxBlock:
    def __init__(self):
        self.checkboxList = {}

    def createRows(self, topLevel, roleDictionary):
        for roleName in roleDictionary:
            self.checkboxList[roleName] = tkinter.Checkbutton(master=topLevel, text=roleName, variable=roleDictionary[roleName])
            self.checkboxList[roleName].grid()

