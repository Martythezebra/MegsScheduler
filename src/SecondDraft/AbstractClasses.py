from abc import ABC, abstractmethod
import enum
class myWindowObject(ABC):
    
    @abstractmethod
    # Display everything at or below this level using .grid(),
    # and run other functions that need to happen at initialization
    def packSelfAndChildren(self) -> None:
        pass

    @abstractmethod
    # Convert this object to a saveable and loadable string
    def toJsonString(self) -> str:
        pass

class Roles(enum.Enum):
    FRANK = "Frank"
    JANET = "Janet"
    BRAD = "Brad"
    RIFF = "Riff"
    MAGENTA = "Magenta"
    COLUMBIA = "Columbia"
    SCOTT = "Dr. Scott"
    ROCKY = "Rocky"
    EDDIE = "Edward"
    CRIM = "Crim"
    TRIXIE = "Trixie"
    HOST = "Host"
    LIGHTS = "Lights"
    CREW = "Crew"