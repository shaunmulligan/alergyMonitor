import os
import query
from init import app
# read environment variables + set defaults
interval = os.getenv('INTERVAL', '1')

print 'Starting Environment Monitor...'
print 'number of records: ' + str(query.count_of_all_type('Temp'))

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
