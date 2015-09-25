# python imports
import psutil
import os, time, datetime

# import sqlchemy refs
from setup_db import Reading, session

# read environment variables + set defaults
interval = os.getenv('INTERVAL', '1')

def log():
    cpu = psutil.cpu_percent()
    newLog = Reading(reading=cpu,timestamp=datetime.datetime.utcnow())
    session.add(newLog)
    session.commit()
    print "CPU: " + str(cpu)

def all_logs():
    readings = session.query(Reading).all()
    for r in readings:
        print "CPU: " + str(r.reading) + ", timestamp: " + str(r.timestamp)

for x in range(0, 20):
    log()
    time.sleep(int(interval))
all_logs()
