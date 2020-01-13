from app import app, db
from app.models import Events
from flask import request
import json


#Create an Event
@app.route('/event', methods = ['POST'])
def add_event():
    data = request.get_json()
    data = json.loads(data)

    event = Events(data['name'], data['address'], data['country'], data['description'])

    db.session.add(event)
    db.session.commit()

    return json.dumps({
                        "response": "New event is created",
                        })

        

#Return all the Events
@app.route('/all-events')
def all_events():

    data = {}
    events = Events.query.all()
    for event in events:
        values = event.__dict__
        data[values['id']] = [{'name' : values['name'],
                                'address' : values['address'],
                                'country' : values['country'],
                                'description' : values['description'],
                                'date' : values['date'].strftime('%b %d %Y')
                                }]

    return json.dumps(data)


#Return a single event
@app.route('/event/<int:id>')
def get_event():

    data = {}
    event = Events.query.get(id)
    values = event.__dict__
    data[values['id']] = [{'name' : values['name'],
                            'address' : values['address'],
                            'country' : values['country'],
                            'description' : values['description'],
                            'date' : values['date'].strftime('%b %d %Y')
                            }]

    return json.dumps(data)


@app.route('/event/<int:id>', methods = ['PUT'])
def update_event(id):

    event = Events.query.get(id)
    
    data = request.get_json()
    data = json.loads(data)

    event.name = data['name']
    event.address = data['address']
    event.country = data['country']
    event.description = data['description']

    db.session.commit()

    data = json.dumps(data)

    return data

@app.route('/event/<int:id>', methods = ['DELETE'])
def delete_event(id):

    event = Events.query.get(id)
    db.session.delete(event)

    db.session.commit()

    data = {}
    data['name'] = event.name
    data['address'] = event.address
    data['country'] = event.country
    data['description'] = event.description
    data['date'] = event.date.strftime('%b %d %Y')

    data = json.dumps(data)
    return data