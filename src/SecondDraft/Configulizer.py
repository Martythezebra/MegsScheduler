# This classes in this file are intended to display a visual representation of a set of cast members,
# and allow the user to edit, save, and load their values.

import json

from AbstractClasses import myWindowObject



class ConfigulizerObject(myWindowObject):

    # Constructor.
    def __init__(self, root = None, dataObject = None) -> None:
        self.myKey = "myValue"
        pass
    


    # Convert this object to a saveable and loadable string
    def toJsonString(self) -> str:
        return json.dumps(self.__dict__)



    # Display everything at or below this level using .grid(),
    # and run other functions that need to happen at initialization
    def packSelfAndChildren(self) -> None:
        pass