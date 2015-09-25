from flask import Flask
import psutil, datetime, time, os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/sensorReadings.db'
db = SQLAlchemy(app)

# read environment variables + set defaults
interval = os.getenv('INTERVAL', '1')

class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    readingType = db.Column(db.String(80))
    reading = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime)

    def __init__(self, readingType, reading, timestamp):
        self.readingType = readingType
        self.reading = reading
        self.timestamp = timestamp

    def __repr__(self):
        return '<Reading %r>' % self.readingType

db.create_all()

def getTemp():
    #this is fake for now...
    return psutil.cpu_percent()

def logCPU():
    cpuPercent = psutil.cpu_percent()
    newLog = Reading(readingType='CPU',reading=cpuPercent,timestamp=datetime.datetime.utcnow())
    db.session.add(newLog)
    db.session.commit()

def logTemp():
    temperature = getTemp()
    newLog = Reading(readingType='Temp',reading=temperature,timestamp=datetime.datetime.utcnow())
    db.session.add(newLog)
    db.session.commit()

def all_logs():
    readings = db.session.query(Reading).all()
    for r in readings:
        print str(r.readingType) + ": " + str(r.reading) + ", timestamp: " + str(r.timestamp)

def print_all_of_type(sensorType):
    readings = get_all_of_type(sensorType)
    for reading in readings:
        print str(reading.readingType) + ": " + str(reading.reading) + ", timestamp: " + str(reading.timestamp)

def get_all_of_type(sensorType):
    return db.session.query(Reading).filter_by(readingType=sensorType).all()

def get_count_of_all_type(sensorType):
    return db.session.query(Reading).filter_by(readingType=sensorType).count()

print 'Starting Environment Monitor...'
print 'number of records: ' + str(get_count_of_all_type('Temp'))
print_all_of_type('Temp')
