# -*- coding: utf-8 -*-
"""
Script to create blank database of "Big 5" and "Other FBS" schools

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 
Base = declarative_base()

db_location = 'sqlite:///FBS_schools.db'
 
class School(Base):
    __tablename__ = 'school'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default="Not Set", nullable=False)
    isPowerFive = Column(Integer, default=1, nullable=False)

def create_db():
 
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine(db_location)
 
    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
    print('School database created')
