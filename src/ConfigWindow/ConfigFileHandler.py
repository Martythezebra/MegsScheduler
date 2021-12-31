import json
import LoadableCastMember
import CastMember

class configSaver:
    def __init__(self, filePath):
        self.myFiles = {}
        self.myFilePath = filePath

    def saveToFile(self, castMember, filename):
        simplifiedObject = {
            "name": castMember.name,
            "roles": castMember.myRoleMatrix
        }

        objString = json.dumps(simplifiedObject, indent=4)

        theFile = open(file=self.myFilePath + filename + ".txt", mode="w")
        theFile.seek(0)
        theFile.write(objString)
        theFile.truncate()
        theFile.close()

    def saveIndexList(self, list) -> None:
        indexFile = open(self.myFilePath + "index\index.txt", "w")

        listJson = json.dumps(list)
        indexFile.seek(0)
        indexFile.write(listJson)
        indexFile.truncate()
        indexFile.close()

class castMemberLoader:
    def __init__(self, filePath) -> None:
        self.myFilePath = filePath

    def loadCastMember(self, filename) -> LoadableCastMember:
        returnedCastMember = LoadableCastMember.LoadableCastMember(filename)

        # Create the file if it does not exist
        theFile = None
        try:
            theFile = open(file=self.myFilePath + filename + ".txt", mode="r")
        except FileNotFoundError:
            defaultCastMember = CastMember.CastMember(filename)
            print("Error!")
            saver = configSaver(filePath=self.myFilePath)
            saver.saveToFile(defaultCastMember, filename)
            theFile = open(file=self.myFilePath + filename + ".txt", mode="r")


        fileContents = theFile.read()
        theFile.close()
        fileObject = json.loads(fileContents)

        returnedCastMember.name = fileObject["name"]
        returnedCastMember.myRoleMatrix = fileObject["roles"]

        return returnedCastMember

    def loadAllFromIndex(self):
        indexFile = open(self.myFilePath + "index\index.txt", "r")
        indexString = indexFile.read()
        print("Index loaded successfully : " + str(indexString))
        indexObject = json.loads(indexString)

        loadedMembers = {} # LoadableCastMember()
        returnedMembers = {} # CastMember()

        for name in indexObject:
            loadedMembers[name] = self.loadCastMember(name)

        for name in loadedMembers:
            tempMember = CastMember.CastMember("placeholder")
            tempMember.configure(loadedMembers[name])
            print("successfully loaded cast member:\n")
            tempMember.toString()
            returnedMembers[name] = tempMember

        return returnedMembers



