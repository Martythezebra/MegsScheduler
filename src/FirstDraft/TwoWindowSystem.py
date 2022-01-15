import tkinter
import ConfigEditor
import Visualizer

class TwoWindowSystem:
    def __init__(self) -> None:
        self.myCfg = ConfigEditor.ConfigEditor()
        self.MyVis = Visualizer.VisualizerTkinterContainer(self.myCfg.castMemberBoxList)

    def begin(self):
        self.myCfg.begin()

        for roleName in self.MyVis.myRolePanes.myPanesList:
            self.MyVis.myRolePanes.myPanesList[roleName].myAvailableCastMemberStringVar.set("Hi Hello Yeet")
        
        self.MyVis.begin()

        self.syncVisualizer()

        self.myCfg.topLevelWindow.mainloop()

    def syncVisualizer(self):
        capability = {}

        for memberBox in self.myCfg.castMemberBoxList:
            capability[memberBox] = self.myCfg.castMemberBoxList[memberBox].myCastMember.outputRoleList()
            #print("Line " + memberBox + " is " + capability[memberBox].__str__())

        self.MyVis.myRolePanes.processRoleMemberAvailability(capability)