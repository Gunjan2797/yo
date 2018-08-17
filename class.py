from flask_sqlalchemy import flask_sqlalchemy

db= SQLAlchemy()

class Flight(db.model):
  __tablename__="flights"
   id=db.Column(db.Integer,primary_key=True)
   origin=db.Column(db.String,nullable=False)
   desination=db.Column(db.String,nullable=False)
   duration=db.Column(db.Integer,nullable=False)

 class Passenger(db.model): 
    __tablename__="passengers"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    flight_id=db.Column(db.Integer, db.ForeignKey("flights.id"),nullable=False)











