from init import db
from model import Reading

def all_of_type(sensorType):
    return db.session.query(Reading).filter_by(readingType=sensorType).all()

def last_x_of_type(x,sensorType):
    return db.session.query(Reading).filter_by(readingType=sensorType).limit(x)

def count_of_all_type(sensorType):
    return db.session.query(Reading).filter_by(readingType=sensorType).count()

def last_hour_of_type(sensorType):
    return -1000

def last_day_of_type(sensorType):
    return -1000

def last_week_of_type(sensorType):
    return -1000

def last_month_of_type(sensorType):
    return -1000
