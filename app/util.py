import query

def print_all_of_type(sensorType):
    readings = query.get_all_of_type(sensorType)
    for reading in readings:
        print str(reading.readingType) + ": " + str(reading.reading) + ", timestamp: " + str(reading.timestamp)
