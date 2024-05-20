from sqlalchemy import (create_engine, Column, String, Integer, Text, schema, func,Date,Float)
from sqlalchemy import (DateTime, MetaData, ForeignKey, Boolean, FLOAT)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker
from datetime import datetime


DEBUG       = False
SCHEMA_NAME = 'world_cities_test'
#DBHOST = 'ksl' # '127.0.0.1' 
DBHOST = '127.0.0.1' 
DBUNAME = 'dbadmin'
PASSWORD = 'mysecret_password'
PORT = '3306'

target_engine = create_engine(f'mysql+pymysql://{DBUNAME}:{PASSWORD}@{DBHOST}:{PORT}/{SCHEMA_NAME}?charset=utf8mb4', echo=DEBUG)
target_metadata = MetaData()
target_base = declarative_base()
Session = sessionmaker(bind=target_engine)

"""
class for my db, each class is a table
"""

class Country(target_base):
    __tablename__  = 't_countries'
    __table_args__ = {"extend_existing": True}
    id             = Column(Integer, primary_key=True)
    country        = Column(String(255), nullable=False)
    iso2           = Column(String(10), nullable=False)
    iso3           = Column(String(10), nullable=False)
    created_on     = Column(DateTime,   nullable=False, default='1970-01-01 01:00:00')    


    def __init__(self, country, iso2,  iso3):
            self.country        = country
            self.iso2           = iso2
            self.iso3           = iso3
            self.created_on     = datetime.now()

class City(target_base):
    __tablename__  = 't_cities'
    __table_args__ = {"extend_existing": True}
    id             = Column(Integer, primary_key=True)
    capital        = Column(String(100), nullable=False)
    city           = Column(String(255), nullable=False) 
    lat            = Column(String(100), nullable=False)
    lng            = Column(String(100), nullable=False)
    admin_name     = Column(String(100), nullable=False)
    city_ascii     = Column(String(100))
    population     = Column(String(255))
    fk_count_id    = Column(Integer, ForeignKey('t_countries.id')) 
    #country        = relationship('Country',foreign_keys=fk_count_id)

    def __init__(self, capital, city, lat, lng, city_ascii, admin_name, population, fk_count_id):
        self.city = city
        self.capital = capital
        self.lat = lat
        self.lng = lng
        self.admin_name = admin_name
        self.city_ascii = city_ascii
        self.population = population
        self.fk_count_id = fk_count_id

class Address(target_base):
    __tablename__  = 't_addresses'
    __table_args__ = {"extend_existing": True}
    id             = Column(Integer, primary_key=True)
    street         = Column(String(255), nullable=False)
    fk_city_id = Column(Integer, ForeignKey('t_cities.id'))
    postal_code    = Column(String(20))
    #country_id     = Column(Integer, ForeignKey('t_countries.id'))
    fk_user_id        = Column(Integer, ForeignKey('t_users.id'))
    #user           = relationship('User')

    def __init__(self, street, city, postal_code, country_id, user_id):
        self.street      = street
        self.city        = city
        self.postal_code = postal_code
        self.country_id  = country_id
        self.user_id     = user_id

class User(target_base):
    __tablename__  = 't_users'
    __table_args__ = {"extend_existing": True}
    id             = Column(Integer, primary_key=True)
    name           = Column(String(100), nullable=False)
    surname        = Column(String(100), nullable=False) 
    username       = Column(String(100), nullable=False)
    email          = Column(String(255), nullable=False)
    phone          = Column(String(255), nullable=False)
    password       = Column(String(100))
    created_on     = Column(DateTime, nullable=False, default='1970-01-01 01:00:00')    

    addresses      = relationship('Address')

    def __init__(self, name, surname, username, email, phone='', password=''):
        self.name       = name
        self.surname    = surname
        self.username   = username
        self.email      = email
        self.phone      = phone
        self.password   = password
        self.created_on = datetime.now()

target_base.metadata.create_all(target_engine)
    


