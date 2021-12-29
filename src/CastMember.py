import tkinter

class CastMember:
    def __init__(self, nameArg):
        # What order would meg like these to be in?
        self.canBrad = False
        self.canColombia = False
        self.canCrew = False
        self.canCrim = False
        self.canEddie = False
        self.canFrank = False
        self.canJanet = False
        self.canLights = False
        self.canMagenta = False
        self.canRiff = False
        self.canRocky = False
        self.canScott = False
        self.canTrixie = False
        

        self.name = nameArg

        self.compatibilityList = {}

        self.incompatibilityList = {}

    # This method is to initialize a CastMember's Attributes from a pre-configured config file
    def configure (self, file):
        print("Placeholder")



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



    # returns a dictionary containing all the boolean members of the class
    def createRoleDictionary (self):

        rolesMatrix = {}

        rolesMatrix["Brad"] = self.canBrad
        rolesMatrix["Colombia"] = self.canColombia
        rolesMatrix["Crew"] = self.canCrew
        rolesMatrix["Crim"] = self.canCrim
        rolesMatrix["Eddie"] = self.canEddie
        rolesMatrix["Frank"] = self.canFrank
        rolesMatrix["Janet"] = self.canJanet
        rolesMatrix["Lights"] = self.canLights
        rolesMatrix["Magenta"] = self.canMagenta
        rolesMatrix["Riff"] = self.canRiff
        rolesMatrix["Rocky"] = self.canRocky
        rolesMatrix["Scott"] = self.canScott
        rolesMatrix["Trixie"] = self.canTrixie

        return rolesMatrix

    def getName(self):
        return self.name