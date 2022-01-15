# This file is intended to serve as the model-in-memory of 
# the various cast members that are currently loaded

import json



class DataStoreObject:

    def __init__(self) -> None:



        pass



    # Convert this object to a saveable and loadable string
    def toJsonString(self) -> str:
        return json.dumps(self.__dict__)