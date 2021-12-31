import tkinter
import json

class CastMember:
    def __init__(self, nameArg):
        # What order would meg like these to be in?
        self.myRoleMatrix = {
            "Brad": False,
            "Colombia": False,
            "Crew": False,
            "Crim": False,
            "Eddie": False,
            "Frank": False,
            "Janet": False,
            "Lights": False,
            "Magenta": False,
            "Riff": False,
            "Rocky": False,
            "Scott": False,
            "Trixie": False,
        }

        self.myTKBoolMatrix = {
            "Brad": tkinter.BooleanVar(value=False),
            "Colombia": tkinter.BooleanVar(value=False),
            "Crew": tkinter.BooleanVar(value=False),
            "Crim": tkinter.BooleanVar(value=False),
            "Eddie": tkinter.BooleanVar(value=False),
            "Frank": tkinter.BooleanVar(value=False),
            "Janet": tkinter.BooleanVar(value=False),
            "Lights": tkinter.BooleanVar(value=False),
            "Magenta": tkinter.BooleanVar(value=False),
            "Riff": tkinter.BooleanVar(value=False),
            "Rocky": tkinter.BooleanVar(value=False),
            "Scott": tkinter.BooleanVar(value=False),
            "Trixie": tkinter.BooleanVar(value=False),
        }

        self.name = nameArg

        self.compatibilityList = {}

        self.incompatibilityList = {}

    # This method is to initialize a CastMember's Attributes from a pre-configured config file
    def configure (self, loadableCastMemberObject):
        self.myRoleMatrix = loadableCastMemberObject.myRoleMatrix
        self.name = loadableCastMemberObject.name
        
        for roleVar in self.myTKBoolMatrix:
            self.myTKBoolMatrix[roleVar].set(self.myRoleMatrix[roleVar])
        print("configured " + self.name)


    # copied from https://pynative.com/make-python-class-json-serializable/
    def toJson(self):
        myString = json.dumps(self.myRoleMatrix, indent=4)
        return myString

    def getName(self) -> str:
        return self.name

    # print to console
    def toString (self):
        print("\t" + self.name + ":")
        print("-------------------------")

        dic = self.createRoleDictionary()

        for key in dic:
            if(len(key) >= 7):
                print(key + ":\t" + str(dic[key]))
            else:
                print(key + ":\t\t" + str(dic[key]))

        print("-------------------------")

    def enableRole(self, roleName):
        self.myRoleMatrix[roleName] = True
    
    def disableRole(self, roleName):
        self.myRoleMatrix[roleName] = False


    # returns a dictionary containing all the boolean members of the class
    def createRoleDictionary (self):
        return self.myRoleMatrix

    def getName(self):
        return self.name