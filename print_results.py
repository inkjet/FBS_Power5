# -*- coding: utf-8 -*-
"""
Script to determine when a college football program from a Power-5 conference
(ACC, SEC, Big Ten, Big 12, Pac-12) plays a non-Power 5 team on the road.
This a semi-rare occurance, 

Requirements: Python with the SQLAlchemy and Beautiful Soup modules

Project page: https://github.com/inkjet/FBS_Power5

Author: Scott Rodkey, rodkeyscott@gmail.com

"""

from create_database import create_db, db_location
from populate_db import populate_db
from calc_matchups import calc_matchups

# Create a blank database -- edit create_database.py to specify a specific DB location
create_db()

# Scrape all FBS schools and their conference from Wikipedia and place them in the database
populate_db(db_location)

# Look at the 2015 schedule and print a week-by-week report to see if a Power-5 school
# is playing a non-Power 5 school on the road
calc_matchups(db_location)