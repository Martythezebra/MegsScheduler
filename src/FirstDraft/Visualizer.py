from tkinter.constants import BROWSE
import ConfigEditor
import tkinter
from tkinter import ttk
import CastMember

class VisualizerTkinterContainer:
    def __init__(self, castMembers = None) -> None:
        self.myCastMembers = castMembers
        self.myMainWindow = tkinter.Toplevel()
        self.myRolePanes = RolePaneGrid(self)

    def begin(self) -> None:
        self.recursivePack()

    def recursivePack(self) -> None:
        self.myRolePanes.recursivePack()

class RolePaneGrid:
    def __init__(self, parent) -> None:
        self.myPanesList = {}
        self.myPaneGridFrame = tkinter.Frame(master=parent.myMainWindow)
        self.myParentVisualizerTkinterContainer = parent

        sacrificialCastMember = CastMember.CastMember("This is only here so I don't have to type out the role list again. Probably should create an enum")

        for role in sacrificialCastMember.myRoleMatrix:
            self.addPane(role)

    def addPane(self, roleName):
        self.myPanesList[roleName] = RolePane(self, roleName)

    def recursivePack(self):
        i = 0
        for child in self.myPanesList:
            self.myPanesList[child].recursivePack(i)
            i += 1

        self.myPaneGridFrame.grid(row=0, column=0)
    
    def processRoleMemberAvailability(self, castMembers):
        self.availabilityLists = castMembers
        self.roleIndexedLists = {
            "Brad": [],
            "Colombia": [],
            "Crew": [],
            "Crim": [],
            "Eddie": [],
            "Frank": [],
            "Janet": [],
            "Lights": [],
            "Magenta": [],
            "Riff": [],
            "Rocky": [],
            "Scott": [],
            "Trixie": [],
        }
        for castMember in self.availabilityLists:
            for roleName in self.availabilityLists[castMember]:
                self.roleIndexedLists[roleName].append(castMember)

        for roleName in self.roleIndexedLists:
            pass#print("Line " + roleName + " is " + self.roleIndexedLists[roleName].__str__())


        for paneName in self.myPanesList:
            self.myPanesList[paneName].updateList(self.roleIndexedLists[paneName])

class RolePane:
    def __init__(self, parent, roleName) -> None:
        self.parentRolePaneGrid = parent
        self.myName = roleName
        self.myPaneFrame = tkinter.Frame(master=parent.myPaneGridFrame)
        self.myNameBox = tkinter.Label(master=self.myPaneFrame, text=self.myName)
        self.myAvailableCastMemberList = []
        self.myAvailableCastMemberStringVar = tkinter.StringVar()
        self.myAvailableCastMemberReadout = tkinter.Listbox(master=self.myPaneFrame, selectmode=BROWSE, listvariable=self.myAvailableCastMemberStringVar)
        
        self.myChosenCastMemberStringVar = tkinter.StringVar()
        self.myChosenCastMemberBox = ttk.Combobox(master=self.myPaneFrame, values=self.myAvailableCastMemberList, textvariable=self.myChosenCastMemberStringVar)
        
    def recursivePack(self, i):
        ROW_LENGTH = 6

        self.myNameBox.grid()
        self.myChosenCastMemberBox.grid()
        self.myAvailableCastMemberReadout.grid()
        self.myAvailableCastMemberStringVar.set("Hello This is a test")
        self.myPaneFrame.grid(row= i // ROW_LENGTH , column= i % ROW_LENGTH)

    def updateList(self, newList):
        myString = ""
        for item in newList:
            myString += item + " "

        print("newlist = ")
        print(newList)

        #print("myString is " + myString)
        self.myAvailableCastMemberList = newList

        self.myChosenCastMemberBox.configure(values=self.myAvailableCastMemberList)

        self.myAvailableCastMemberStringVar.set(myString)
