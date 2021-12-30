import tkinter
import json

class LoadableCastMember:
    def __init__(self, nameArg):
        
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
    
    def toString (self):
        print("\t" + self.name + ":")
        print("-------------------------")

        for key in self.myRoleMatrix:
            if(len(key) >= 7):
                print(key + ":\t" + str(self.myRoleMatrix[key]))
            else:
                print(key + ":\t\t" + str(self.myRoleMatrix[key]))

        print("-------------------------")