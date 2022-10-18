import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person) """

""" class Item(Base):
    __tablename__ = 'item'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250)) """

class People(Base):
    __tablename__ = 'people'
    uid = Column(Integer, primary_key=True)
    name = Column(String(250))
    heigth = Column(Float)
    mass = Column(Float)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(Date)
    gender = Column(String(50))
    created = Column(Date)
    edited = Column(Date)
    homeworld = Column(String(250))
    url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    uid = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Float)
    rotation_period = Column(Float)
    rotation_period = Column(Float)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    created = Column(Date)
    edited = Column(Date)
    url = Column(String(250))

class Starship(Base):
    __tablename__ = 'starship'
    uid = Column(Integer, primary_key=True)
    model = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(Float)
    mglt = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(100))
    pilots = Column(ARRAY(String))
    created = Column(Date)
    edited = Column(Date)
    url = Column(String(250))


    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e