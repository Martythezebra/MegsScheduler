import json
import AbstractClasses



class CastMemberObject:
    
    def __init__(self) -> None:

        self.myRoleData = {}
        for role in AbstractClasses.Roles:
            self.myRoleData[role] = False



    def toJsonString(self) -> str:
        # return json.dumps(self.__dict__)
        return str(self.myRoleData)