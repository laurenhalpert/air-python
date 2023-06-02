from sqlalchemy import create_engine, func, MetaData
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Reservation(Base):
    __tablename__= 'reservations'

    id = Column(Integer(), primary_key = True)
    reference_code = Column(String())
    passenger_id = Column(ForeignKey('passengers.id'))
    flight_id = Column(ForeignKey('flights.id'))

    def __repr__(self):
        return(f'Reservation: {self.reference_code}')


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer(), primary_key = True)
    departure_city = Column(String())
    arrival_city = Column(String())
    plane_type = Column(String())
    cost = Column(Integer())

    reservations = relationship('Reservation', backref='flight')
    passengers = association_proxy('reservations', 'passenger', creator=lambda px: Reservation(passenger=px))

    
    def __repr__(self):
        return(f'Flight number {self.id} is going from {self.departure_city} to {self.arrival_city} on a {self.plane_type}, and costs ${self.cost}.')

class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())
    budget = Column(Integer())
    
    reservations = relationship('Reservation', backref='passenger')
    flights = association_proxy('reservations', 'flight', creator = lambda ft: Reservation(flight = ft))

    def __repr__(self):
        return f'Passenger: {self.name} Age: {self.age} Budget: ${self.budget}'