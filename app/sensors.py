import psutil, datetime
from init import db
from model import Reading

def getTemp():
    #this is fake for now...
    return psutil.cpu_percent()

def getHumidity():
    #this is fake for now...
    return psutil.cpu_percent()

def getAirQuality():
    #this is fake for now...
    return psutil.cpu_percent()

def getDustLevel():
    #this is fake for now...
    return psutil.cpu_percent()

def saveTemp():
    newTemp = getTemp()
    newReading = Reading(readingType='Temperature',reading=newTemp,timestamp=datetime.datetime.utcnow())
    db.session.add(newReading)
    db.session.commit()
