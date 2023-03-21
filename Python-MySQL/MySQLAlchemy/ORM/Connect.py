#!/usr/bin/python3
from sqlalchemy import create_engine

#Creating an Enging
engine = create_engine('mysql://root:admin@localhost/Cookie_Store')

#Creating the connection
connection = engine.connect()

