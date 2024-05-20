#!/usr/bin/python
# db_set.py
# Made by Amendola Lorenzo 2024_05_16
"""
Script to create database schema and establish connection using SQLAlchemy.

Author: Amendola Lorenzo
Date: 2024_05_16

This script imports necessary modules from SQLAlchemy to create a database schema,
including necessary data types, relationships, and session management. It also establishes
a connection to the MySQL database server.

Instructions:
1. Modify the configuration parameters such as DEBUG, SCHEMA_NAME, DBHOST, DBUNAME, PASSWORD, and PORT as needed.
2. Run the script to create the database schema and establish the connection.

Usage:
- Make sure to have SQLAlchemy and pymysql installed.
- Run this script using Python 3.

"""

from sqlalchemy import (create_engine, Column, String, Integer, Text, schema, func, Date)
from sqlalchemy import (DateTime, MetaData, ForeignKey, Boolean, FLOAT)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DEBUG = True
SCHEMA_NAME = 'world_cities_test'
# DBHOST = 'ksl' # '127.0.0.1'
DBHOST = '127.0.0.1' 
DBUNAME = 'dbadmin'
PASSWORD = 'mysecret_password'
PORT = '3306'

# Crea il motore di connessione al database utilizzando i parametri forniti
engine = create_engine(f'mysql+pymysql://{DBUNAME}:{PASSWORD}@{DBHOST}:{PORT}', echo=DEBUG)

# Stabilisce una connessione con il database
conn = engine.connect()

# Verifica se lo schema esiste, se non esiste lo crea
if SCHEMA_NAME not in conn.dialect.get_schema_names(conn):
    conn.execute(schema.CreateSchema(SCHEMA_NAME)) # crea lo schema se non esiste

# Chiude la connessione
conn.close()

# Dispose del motore di connessione
engine.dispose()
