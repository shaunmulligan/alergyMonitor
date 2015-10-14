from environmentMonitor import db

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
