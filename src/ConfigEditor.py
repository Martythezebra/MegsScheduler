import tkinter
from tkinter.constants import FALSE, TRUE
import CastMember
import ConfigFileHandler
import functools


class ConfigEditor:
    def __init__(self):
        self.topLevelWindow = tkinter.Tk()
        self.castMemberBoxList = {}
        self.castMemberFrame = tkinter.Frame()
        self.myTopBar = TopBar(self)
        self.myFileWriter = ConfigFileHandler.configSaver(".\config\TestCastMembers\\")
        self.myConfigLoader = ConfigFileHandler.castMemberLoader(".\config\TestCastMembers\\")
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

    def saveAllButtonClicked(self, event):
        print("Save clicked")

        indexNameList = []

        for memberBoxKey in self.castMemberBoxList:
            castMember = self.castMemberBoxList[memberBoxKey].myCastMember
            print("Member name is " + castMember.name)
            self.myFileWriter.saveToFile(castMember, castMember.name)
            indexNameList.append(memberBoxKey)

        self.myFileWriter.saveIndexList(indexNameList)
    
    def loadAllButtonClicked(self, event):
        print("Load clicked")

        castMembersToLoad = self.myConfigLoader.loadAllFromIndex()

        for castMember in castMembersToLoad:
            self.addCastMember(castMembersToLoad[castMember])

        self.begin()

class TopBar:
    def __init__(self, parent):
        self.bar = tkinter.Frame()
        self.parent = parent
    
    def createButtons(self):
        self.savebutton = tkinter.Button(master=self.bar, text="Save All")
        self.savebutton.bind("<ButtonRelease-1>", self.parent.saveAllButtonClicked)
        self.savebutton.grid(row=0, column=0)

        self.filebutton = tkinter.Button(master=self.bar, text="File (placeholder)")
        self.filebutton.bind("<ButtonRelease-1>", self.parent.loadAllButtonClicked)
        self.filebutton.grid(row=0, column=1)

        self.bar.grid(row=0)



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
        self.myCheckboxes.createRows(self.castMemberBoxWindow, self.myCastMember.myRoleMatrix)
        self.updateBoolsOnStart()
    
    def updateBoolsOnClick(self, roleKey):
        print("checkbox clicked: " + self.myCastMember.name + " " + roleKey + ". Value updated to " + str(self.myCastMember.myTKBoolMatrix[roleKey].get()))
        
        boolVal = self.myCastMember.myTKBoolMatrix[roleKey].get()
        boolVal = boolVal
        self.myCastMember.myRoleMatrix[roleKey] = boolVal

    def updateBoolsOnStart(self):
        for roleKey in self.myCastMember.myRoleMatrix:
            self.myCastMember.myRoleMatrix[roleKey] = self.myCastMember.myTKBoolMatrix[roleKey].get()   
            print("Initialized: " + self.myCastMember.name + " " + roleKey + ". Value updated to " + str(self.myCastMember.myRoleMatrix[roleKey]))




class CheckboxBlock:
    def __init__(self, parent):
        self.checkboxList = {}
        self.myParent = parent

    def createRows(self, topLevel, roleDictionary):
        for roleName in roleDictionary:
            # https://www.delftstack.com/howto/python-tkinter/how-to-pass-arguments-to-tkinter-button-command/
            # See the above for checkbox command help, regarding "partials"
            self.checkboxList[roleName] = tkinter.Checkbutton(master=topLevel, text=roleName, name="a" + roleName, variable=self.myParent.myCastMember.myTKBoolMatrix[roleName], offvalue=FALSE, onvalue=TRUE, command=functools.partial(self.myParent.updateBoolsOnClick, roleName))
            self.checkboxList[roleName].grid()

