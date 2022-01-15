# This allows the user to display a selected result. Plans in the future include 
# ability to filter and/or query permutations of the input data, possibly with 
# reference to weightings (?)

import json

from AbstractClasses import myWindowObject

class VisualizerObject(myWindowObject):

    def __init__(self, root = None, dataObject = None) -> None:
        pass



    # Convert this object to a saveable and loadable string
    def toJsonString(self) -> str:
        return json.dumps(self.__dict__)

    

    # Display everything at or below this level using .grid(),
    # and run other functions that need to happen at initialization
    def packSelfAndChildren(self) -> None:
        pass