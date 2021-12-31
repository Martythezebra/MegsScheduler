import CastMember
import ConfigEditor

# Should produce 6 cast members, each with a checkbox for each role.

myCfg = ConfigEditor.ConfigEditor()

people = {}

people["A"] = CastMember.CastMember("Tim")

people["A"].enableRole("Brad")
people["A"].enableRole("Lights")
people["A"].enableRole("Colombia")

people["B"] = CastMember.CastMember("Jane")

people["C"] = CastMember.CastMember("Gib")

people["D"] = CastMember.CastMember("Fork")

people["E"] = CastMember.CastMember("Spoon")

people["F"] = CastMember.CastMember("Knife")

myCfg.addCastMember(people["A"])
myCfg.addCastMember(people["B"])
myCfg.addCastMember(people["C"])
myCfg.addCastMember(people["D"])
myCfg.addCastMember(people["E"])
myCfg.addCastMember(people["F"])

myCfg.begin()