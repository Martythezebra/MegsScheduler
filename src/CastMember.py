import tkinter


import tkinter

class CastMember:
#
# Begin definitions
#
    def __init__(self, nameArg):
        # What order would meg like these to be in?
        self.canMagenta = False
        self.canRiff = False
        self.canColombia = False
        self.canBrad = False
        self.canJanet = False
        self.canEddie = False
        self.canFrank = False
        self.canScott = False
        self.canRocky = False
        self.canCrew = False
        self.canLights = False
        self.canCrim = False
        self.canTrixie = False
        

        self.name = nameArg

        self.compatibilityList = {}

        self.incompatibilityList = {}

    # This method is to initialize a CastMember's Attributes from a pre-configured config file
    def configure (self, file):
        print("Placeholder")


class CastBox:

    def __init__(self, nameArg, theWindow):
        self.member = CastMember(nameArg)
        self.box = tkinter.Label(theWindow).grid()
        tkinter.Checkbutton(self.box, text="Rocky", variable=self.member.canRocky).grid(row=0, sticky="W")
        tkinter.Checkbutton(self.box, text="two", variable=self.member.canRocky).grid(row=1, sticky="W")
        tkinter.Checkbutton(self.box, text="three", variable=self.member.canRocky).grid(row=2, sticky="W")
        tkinter.Checkbutton(self.box, text="four", variable=self.member.canRocky).grid(row=3, sticky="W")
        tkinter.Checkbutton(self.box, text="Rocky again", variable=self.member.canRocky).grid(row=4, sticky="W")
