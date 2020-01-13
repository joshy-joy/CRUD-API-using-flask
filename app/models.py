from app import db
from datetime import datetime


class Events(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(500))
    address = db.Column(db.String(500))
    country = db.Column(db.String(100))
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime, nullable = False, 
                    default=datetime.utcnow, 
                    onupdate = datetime.utcnow)


    def __init__(self, name, address, country, description):
        self.name = name
        self.address = address
        self.country = country
        self.description = description

        

