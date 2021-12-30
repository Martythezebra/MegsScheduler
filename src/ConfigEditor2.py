import tkinter



# cfg
class ConfigEditor2: 
    def __init__(self) -> None:
        self.cfgWindow = tkinter.Tk()
        
        self.cfgTopBar = TopBar(self)
        self.cfgMemberPanes = MemberPaneGrid(self)
    
    def beginWindow(self):
        self.cfgTopBar.initializeWindow()
        self.cfgMemberPanes.initializeWindow()



# tpb
class TopBar: 
    def __init__(self, parent) -> None:
        self.parentConfigEditor2 = parent
        self.tpbFrame = tkinter.Frame(master=parent.cfgWindow)

    def toJSON(self) -> str:
        # TODO: Convert members to be saved in file
        pass



# mpg
class MemberPaneGrid:
    def __init__(self, parent) -> None:
        self.parentConfigEditor2 = parent
        self.mpgFrame = tkinter.Frame(master=parent.cfgWindow)
        
        self.mpgMembers = {}

    def addMemberToGrid(self, castMemberObject) -> None:
        newPane = MemberPane(self)
        newPane.loadDataFrom(castMemberObject)
        self.mpgMembers[castMemberObject.name] = newPane

    def toJSON(self) -> str:
        # TODO: Convert members to be saved in file
        pass

# mem
class MemberPane:
    def __init__(self, parent) -> None:
        self.parentMemberPaneGrid = parent
        self.mpgCheckBoxGroup = MemberCheckboxGroup()
        self.memCastMemberObject = None
        self.memName = None

    # Only to be called after checkboxes are initialized
    def loadDataFrom(self, castMemberObject) -> None:
        self.memCastMemberObject = castMemberObject
        self.memName = castMemberObject.getName()
    
    def toJSON(self) -> str:
        # TODO: Convert members to be saved in file
        pass

# cbg
class MemberCheckboxGroup:
    def __init__(self, parent) -> None:
        self.parentMemberPane = parent

    def toJSON(self) -> str:
        # TODO: Convert members to be saved in file
        pass

# chk
class CheckBox:
    def __init__(self, parent) -> None:
        self.parentMemberPane = parent

    def toJSON(self) -> str:
        # TODO: Convert members to be saved in file
        pass