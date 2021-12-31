import CastMember
import ConfigEditor
import ConfigFileHandler

myCfg = ConfigEditor.ConfigEditor()
myFileHandler = ConfigFileHandler.configSaver()
people = {}

people["A"] = CastMember.CastMember("Tim")

people["A"].enableRole("Brad")
people["A"].enableRole("Brad")
people["A"].enableRole("Lights")
people["A"].enableRole("Colombia")

people["B"] = CastMember.CastMember("Jane")

people["C"] = CastMember.CastMember("Gib")

people["D"] = CastMember.CastMember("Fork")

people["E"] = CastMember.CastMember("Spoon")

people["F"] = CastMember.CastMember("Knife")

for person in people:
    myFileHandler.saveToFile(people[person], people[person].name)