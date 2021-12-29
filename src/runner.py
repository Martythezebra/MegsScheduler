import CastMember
import ConfigEditor

myCfg = ConfigEditor.ConfigEditor()

personA = CastMember.CastMember("Tim")

personA.enableRole("Brad")
personA.enableRole("Brad")
personA.enableRole("Lights")
personA.enableRole("Colombia")

personB = CastMember.CastMember("Jane")

personC = CastMember.CastMember("Gib")

personD = CastMember.CastMember("Fork")

personE = CastMember.CastMember("Spoon")

personF = CastMember.CastMember("Knife")

myCfg.addCastMember(personA)
myCfg.addCastMember(personB)
myCfg.addCastMember(personC)
myCfg.addCastMember(personD)
myCfg.addCastMember(personE)
myCfg.addCastMember(personF)

myCfg.begin()