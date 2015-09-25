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

def logCPU():
    cpuPercent = psutil.cpu_percent()
    newLog = Reading(readingType='CPU',reading=cpuPercent,timestamp=datetime.datetime.utcnow())
    db.session.add(newLog)
    db.session.commit()

def logTemp():
    cpuPercent = psutil.cpu_percent()
    newLog = Reading(readingType='Temp',reading=cpuPercent,timestamp=datetime.datetime.utcnow())
    db.session.add(newLog)
    db.session.commit()

def all_logs():
    readings = db.session.query(Reading).all()
    for r in readings:
        print str(r.readingType) + ": " + str(r.reading) + ", timestamp: " + str(r.timestamp)

def print_all_of_type(sensorType):
    readings = db.session.query(Reading).filter_by(readingType=sensorType).limit(40)
    for reading in readings:
        print str(reading.readingType) + ": " + str(reading.reading) + ", timestamp: " + str(reading.timestamp)

def get_count_of_all_type(sensorType):
    return db.session.query(Reading).filter_by(readingType=sensorType).count()

# for x in range(0, 4):
#     logCPU()
#     time.sleep(int(interval))
#
# for x in range(0, 8):
#     logTemp()
#     time.sleep(int(interval))
# all_logs()
print get_count_of_all_type('Temp')
print_all_of_type('Temp')
