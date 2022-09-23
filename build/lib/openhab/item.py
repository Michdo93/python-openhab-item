from datetime import datetime
import base64
import io
import cv2
from imageio.v2 import imread
import numpy as np

class Item(object):
    def __init__(self, type:str, name:str, state = None, tags:list = None, groups:list = None):
        self.__itemTypes = ["Color", "Contact", "DateTime", "Dimmer", "Group", "Image", "Location", "Number", "Player", "Rollershutter", "String", "Switch"]
        self.setType(type)
        self.setName(name)
        self.setState(state)
        self.setTags(tags)
        self.setGroups(groups)
        
    def __checkItemValue(self, type:str, value):
        bool = False

        if type == self.__itemTypes[0]:
            bool = self.__checkColorValue(value)
        elif type == self.__itemTypes[1]:
            bool = self.__checkContactValue(value)
        elif type == self.__itemTypes[2]:
            bool = self.__checkDateTimeValue(value)
        elif type == self.__itemTypes[3]:
            bool = self.__checkDimmerValue(value)
        elif type == self.__itemTypes[4]:
            bool = self.__checkGroupValue(value)
        elif type == self.__itemTypes[5]:
            bool = self.__checkImageValue(value)
        elif type == self.__itemTypes[6]:
            bool = self.__checkLocationValue(value)
        elif type == self.__itemTypes[7]:
            bool = self.__checkNumberValue(value)
        elif type == self.__itemTypes[8]:
            bool = self.__checkPlayerValue(value)
        elif type == self.__itemTypes[9]:
            bool = self.__checkRollershutterValue(value)
        elif type == self.__itemTypes[10]:
            bool = self.__checkStringValue(value)
        elif type == self.__itemTypes[11]:
            bool = self.__checkSwitchValue(value)

        return bool

    def __checkColorValue(self, value):
        if isinstance(value, str):
            if value == "ON" or value == "OFF" or value == "INCREASE" or value == "DECREASE":
                return True
            else:
                value = value.replace(" ", "")
                splitted = value.split(",")
                hue = float(splitted[0])
                saturation = float(splitted[1])
                brightness = float(splitted[2])
                if isinstance(hue, float) or isinstance(saturation, float) or isinstance(brightness, float):
                    if (0 <= hue <= 360.0) and (0 <= saturation <= 255.0) and (0 <= brightness <= 255.0):
                        return True
                    return False
                return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False
        return False

    def __checkContactValue(self, value):
        if isinstance(value, str):
            if value == "OPEN" or value == "CLOSED":
                return True
            return False
        return False

    def __checkDateTimeValue(self, value):
        if isinstance(value, str):
            if value != datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%dT%H:%M:%SZ'):
                return True
            return False
        return False

    def __checkDimmerValue(self, value):
        if isinstance(value, str):
            if value == "ON" or value == "OFF" or value == "INCREASE" or value == "DECREASE":
                return True
            return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False

    def __checkGroupValue(self, value):
        if isinstance(value, str):
            return True
        return False

    def __checkImageValue(self, value):
        if base64.b64decode(value, validate=True) == True:
            return True
        return False

    def __checkLocationValue(self, value):
        if isinstance(value, str):
            value = value.replace(" ", "")
            splitted = value.split(",")
            latitude = float(splitted[0])
            longitude = float(splitted[1])
            altitude = float(splitted[2])
            if isinstance(latitude, float) or isinstance(longitude, float) or isinstance(altitude, float):
                return True
            return False
        return False

    def __checkNumberValue(self, value):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False

    def __checkPlayerValue(self, value):
        if value == "PLAY" or value == "PAUSE" or value == "NEXT" or value == "PREVIOUS" or value == "REWIND" or value == "FASTFORWARD":
            return True
        return False

    def __checkRollershutterValue(self, value):
        if isinstance(value, str):
            if value == "UP" or value == "DOWN" or value == "STOP" or value == "MOVE":
                return True
            return False
        elif isinstance(value, int):
            if 0 <= value <= 100:
                return True
            return False

    def __checkStringValue(self, value):
        if isinstance(value, str):
            return True
        return False

    def __checkSwitchValue(self, value):
        if value == "ON" or value == "OFF":
            return True
        return False
    
    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
    
    def getState(self):
        return self.state
    
    def getTags(self):
        return self.tags
    
    def getGroups(self):
        return self.groups
    
    def setType(self, type:str):
        if self.__checkItemType(type):
            self.type = type
        
    def setName(self, name:str):
        self.name = name
        
    def setState(self, state):
        if self.__checkItemValue:
            self.state = state
        
    def setTags(self, tags:list):
        self.tags = tags
        
    def setGroups(self, groups:list):
        self.groups = groups

class ColorItem(Item):
    def __init__(self, name:str, state = None, tags:list = None, groups:list = None):
        super().__init__("Color", name, state, tags, groups)
        
    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
    
    def getHSB():
        return self.getState().split(",")
    
    def getHue():
        return self.getState().split(",")[0]
    
    def getSaturation():
        return self.getState().split(",")[1]
    
    def getBrightness():
        return self.getState().split(",")[2]

    def setHSB(hsb:list):
        self.setState(hsb[0] + "," + hsb[1] + "," + hsb[2])
        
    def setHue(hue:float):
        hsb = self.getHSB()
        
        if (0 <= hue <= 360.0):
            hsb[0] = hue
            self.setHSB(hsb)
        
    def setSaturation(saturation:float):
        hsb = self.getHSB()
        
        if (0 <= saturation <= 360.0):
            hsb[1] = saturation
            self.setHSB(hsb)
        
    def setBrightness(brightness:float):
        hsb = self.getHSB()
        
        if (0 <= brightness <= 360.0):
            hsb[2] = brightness
            self.setHSB(hsb)
    
    def validate(self, value):
        return super().__checkColorValue(value)
        
class ContactItem(Item):
    def __init__(self, name:str, state:str = None, tags:list = None, groups:list = None):
        super().__init__("Contact", name, state, tags, groups)

    def setState(state:str):
        super().setState(state)

    def getState():
        return super().getState()
    
    def toggleState():
        if self.getState() == "OPEN":
            self.setState("CLOSED")
        else:
            self.setState("OPEN")
        
    def validate(self, value):
        return super().__checkContactValue(value)
        
class DateTimeItem(Item):
    def __init__(self, name:str, state:datetime = None, tags:list = None, groups:list = None):
        super().__init__("DateTime", name, state, tags, groups)

    def setState(state:str):
        super().setState(state)

    def getState():
        return super().getState()
    
    def setDatetime(state:datetime):
        super().setState(state.strftime('%Y-%m-%dT%H:%M:%SZ'))
    
    def getDatetime():
        return datetime.strptime(str(super().getState()), '%Y-%m-%dT%H:%M:%S.%f%z')
        
    def validate(self, value):
        return super().__checkDateTimeValue(value)
        
class DimmerItem(Item):
    def __init__(self, name:str, state:int = None, tags:list = None, groups:list = None):
        super().__init__("Dimmer", name, state, tags, groups)

    def setState(state:int):
        super().setState(state)

    def getState():
        return int(super().getState())
        
    def validate(self, value):
        return super().__checkDimmerValue(value)
        
class GroupItem(Item):
    def __init__(self, name:str, state:str = None, tags:list = None, groups:list = None):
        super().__init__("Group", name, state, tags, groups)

    def getState():
        return super().getState()
        
    def validate(self, value):
        return super().__checkGroupValue(value)
        
class ImageItem(Item):
    def __init__(self, name:str, state:str = None, tags:list = None, groups:list = None):
        super().__init__("Image", name, state, tags, groups)

    def setState(state:str):
        super().setState(state)

    def getState():
        return super().getState()
    
    def getNumpyImage():
        return imread(io.BytesIO(base64.b64decode(self.getState())))
    
    def getCV2Image():
        return cv2.cvtColor(self.getNumpyImage(), cv2.COLOR_RGB2BGR)
    
    def setNumpyImage(state):
        self.setState(state.tobytes())
        
    def setCV2Image(state):
        retval, buffer = cv2.imencode('.jpg', state)
        self.setNumpyImage(buffer)
        
    def validate(self, value):
        if isinstance(value, numpy.ndarray):
            retval, buffer = cv2.imencode('.jpg', value)
            if isinstance(buffer, bytes):
                value = buffer
            value = value.tobytes()

        if isinstance(value,str):
            return super().__checkImageValue(value)
        else:
            return False
        
class LocationItem(Item):
    def __init__(self, name:str, state = None, tags:list = None, groups:list = None):
        super().__init__("Location", name, state, tags, groups)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
    
    def getGPS():
        return self.getState().split(",")
    
    def getLongitude():
        return float(self.getState().split(",")[0])
    
    def getLatitude():
        return float(self.getState().split(",")[1])
    
    def getAltitude():
        return float(self.getState().split(",")[2])
    
    def setGPS(gps:list):
        self.setState(gps[0] + "," + gps[1] + "," + gps[2])
        
    def setLongitude(longitude:float):
        gps = self.getGPS()
        
        gps[0] = longitude
        self.setGPS(GPS)
        
    def setLatitude(latitude:float):
        gps = self.getGPS()
        
        gps[1] = latitude
        self.setGPS(GPS)
        
    def setAltitude(altitude:float):
        gps = self.getGPS()

        gps[2] = altitude
        self.setGPS(GPS)
            
    def validate(self, value):
        return super().__checkLocationValue(value)
        
class NumberItem(Item):
    def __init__(self, name:str, state = None, tags:list = None, groups:list = None):
        super().__init__("Number", name, self.__numberValue(state), tags, groups)

    def setState(state):
        super().setState(self.__numberValue(state))

    def getState():
        return self.__numberValue(super().getState())
            
    def __numberValue(self, value):
        if "." in value:
            return float(value)
        else:
            return int(value)
        
    def validate(self, value):
        return super().__checkNumberValue(value)
        
class PlayerItem(Item):
    def __init__(self, name:str, state:str = None, tags:list = None, groups:list = None):
        super().__init__("Player", name, state, tags, groups)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def validate(self, value):
        return super().__checkPlayerValue(value)
        
class RollershutterItem(Item):
    def __init__(self, name:str, state:str = None, tags:list = None, groups:list = None):
        super().__init__("Rollershutter", name, state, tags, groups)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def validate(self, value):
        return super().__checkRollershutterValue(value)
        
class StringItem(Item):
    def __init__(self, name:str, state:str = None, tags:list = None, groups:list = None):
        super().__init__("String", name, state, tags, groups)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
        
    def validate(self, value):
        return super().__checkStringValue(value)

class SwitchItem(Item):
    def __init__(self, name:str, state:str = None, tags:list = None, groups:list = None):
        super().__init__("Switch", name, state, tags, groups)

    def setState(state):
        super().setState(state)

    def getState():
        return super().getState()
    
    def toggleState():
        if self.getState() == "ON":
            self.setState("OFF")
        else:
            self.setState("ON")
        
    def validate(self, value):
        return super().__checkSwitchValue(value)

