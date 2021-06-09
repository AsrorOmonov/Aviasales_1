import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

flights = [
    {
        'id': '1',
        'origin': 'SVO',
        'destination': 'BKK',
        'departure_date': '20210701',
        'departure_time': '2010',
        'arrival_date': '20210702',
        'arrival_time': '1115',
        'number': 'SU-275',
    },
    {
        'id': '2',
        'origin': 'SVO',
        'destination': 'BKK',
        'departure_date': '20210702',
        'departure_time': '2010',
        'arrival_date': '20210703',
        'arrival_time': '1115',
        'number': 'SU-275',
    },
    {
        'id': '3',
        'origin': 'SVO',
        'destination': 'BKK',
        'departure_date': '20210703',
        'departure_time': '2010',
        'arrival_date': '20210704',
        'arrival_time': '1115',
        'number': 'SU-275',
    },
    {
        'id': '4',
        'origin': 'SVO',
        'destination': 'BKK',
        'departure_date': '20210704',
        'departure_time': '2010',
        'arrival_date': '20210705',
        'arrival_time': '1115',
        'number': 'SU-275',
    },
    {
        'id': '6',
        'origin': 'SVO',
        'destination': 'BKK',
        'departure_date': '20210705',
        'departure_time': '2010',
        'arrival_date': '20210706',
        'arrival_time': '1115',
        'number': 'SU-275',
    },
    {
        'id': '7',
        'origin': 'SVO',
        'destination': 'BKK',
        'departure_date': '20210706',
        'departure_time': '2010',
        'arrival_date': '20210707',
        'arrival_time': '1115',
        'number': 'SU-275'
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our web service</h1>
<p>"/flight/all" -> this url shows you all the info exists in JSON</p>
    -- "/flight?id='id number' -> this url shows all info related to an id number you select"'''


@app.route('/flights/all', methods=['GET'])
def api_all():
    return jsonify(flights)


@app.route('/flights', methods=['GET'])
def api_by_id():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."

    for flight in flights:

        if flight['id'] == id:
            return f'''ORIGIN:  ({flight["origin"]})\n -- 
              DESTINATION:  ( {flight["destination"]})\n --    
             DEPARTURE_DATE:     ({flight["departure_time"]})\n --
             DEPARTURE_TIME:  ({flight["departure_time"]})\n --
             ARRIVAL_DATE:    ({flight["arrival_date"]})\n --
             ARRIVAL_TIME:  ({flight["arrival_time"]})\n --
             NUMBER:  ({flight["number"]})\n
             '''

    else:
        return '404 Not found'


app.run()
