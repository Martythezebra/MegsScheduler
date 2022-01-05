from CastMember import CastMember
import ConfigEditor
import ConfigFileHandler 
import ConfigEditor


myConfigEditor = ConfigEditor.ConfigEditor()
myLoader = ConfigFileHandler.castMemberLoader(".\config\TestCastMembers\\")

myPerson = myLoader.loadCastMember("Fork")

myCastMember = CastMember("JIMBO babey")

myCastMember.configure(myPerson)

myConfigEditor.addCastMember(myCastMember)
myConfigEditor.begin()