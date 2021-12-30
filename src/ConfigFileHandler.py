import json

class configSaver:
    def __init__(self):
        self.myFiles = {}

    def openFile(self, fileName):
        if fileName not in self.myFiles:
            self.myFiles[fileName] = open(file=".\config\TestCastMembers\\" + fileName + ".txt", mode="w")

        return self.myFiles[fileName]

    def closeFile(self, currentOpenFile):
        pass

    def saveToFile(self, object, filename):
        objString = json.dumps(object.__dict__)

        self.openFile(filename)
        
        self.myFiles[filename].write(objString)