# This is the interface between this project and the outside world. This controls
# what happens in the Configulizer, Visualizer, and DataStore.

import json
import AbstractClasses
import Configulizer
import Visualizer
import StoreCastMember
import DataStore
import tkinter



class OverlordObject(AbstractClasses.myWindowObject):

    def __init__(self) -> None:

        self.myRoot = tkinter.Tk()
        self.myData = DataStore.DataStoreObject()
        self.myCfg = Configulizer.ConfigulizerObject(root=self.myRoot, dataObject=self.myData)
        self.myVis = Visualizer.VisualizerObject(root=self.myRoot, dataObject=self.myData)



    # Convert this object to a saveable and loadable string
    def toJsonString(self) -> str:
        return json.dumps(self.__dict__)



    # Display everything at or below this level using .grid(),
    # and run other functions that need to happen at initialization
    def packSelfAndChildren(self) -> None:
        pass



    def addCastMember(self, castMemberObject) -> None:
        # Add cast member to data store list
        # Update Configulizer
        # Update Visulizer
        pass

    def loadCastMemberFromFile(self, uniqueName) -> StoreCastMember.CastMemberObject:
        pass