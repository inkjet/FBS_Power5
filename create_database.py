# -*- coding: utf-8 -*-
"""
Script to create blank database of "Big 5" and "Other FBS" schools

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os
 
Base = declarative_base()

db_folder = os.getcwd() + '/FBS_schools.db'
db_location = 'sqlite:///' + db_folder
 
class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default="Not Set", nullable=False)
    isPowerFive = Column(Integer, default=1, nullable=False)

def create_db():
    engine = create_engine(db_location)
    Base.metadata.create_all(engine)
    print('School database created at %s' % db_folder)
    print(' ')
