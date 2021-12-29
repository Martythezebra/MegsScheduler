import tkinter

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

    def enableRole(self, roleName):
        self.myRoleMatrix[roleName] = True
    
    def disableRole(self, roleName):
        self.myRoleMatrix[roleName] = False


    # returns a dictionary containing all the boolean members of the class
    def createRoleDictionary (self):
        return self.myRoleMatrix

    def getName(self):
        return self.name