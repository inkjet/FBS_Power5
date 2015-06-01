# -*- coding: utf-8 -*-
"""
Script to populate the database of "Big 5" and "Other FBS" schools

Uses example of scraping a Wikipedia table as documented here:
http://adesquared.wordpress.com/2013/06/16/using-python-beautifulsoup-to-scrape-a-wikipedia-table/

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bs4 import BeautifulSoup
import urllib2
 
from create_database import School

def populate_db(db_location):

    engine = create_engine(db_location)
    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    School.metadata.bind = engine
     
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
     
     # now scrape the school names from Wikipedia
    url="http://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_programs"
    page=urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    
    table = soup.find("table", { "class" : "wikitable sortable" })
    
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        #For each "tr", assign each "td" to a variable.
        if len(cells) == 8:
            schoolName = cells[0].findAll(text=True)
            schoolConference = cells[4].find(text=True)
             # Insert school name into table
            schoolNameText = ''.join(schoolName)
            # Some school are listed as <full school name> !<abbreviation>  We want the abbreviated name
            ex_loc = schoolNameText.find('!')
            if ex_loc > 0:
                schoolNameText = schoolNameText[ex_loc+1:]
            # check if they're a power 5 conference
            if schoolConference == 'ACC' or \
               schoolConference == 'Big Ten' or \
               schoolConference == 'Big 12' or \
               schoolConference == 'Pac-12' or \
               schoolConference == 'SEC':           
                new_school = School(isPowerFive=1, name=schoolNameText)
                status = ''.join([schoolNameText, " is a Power 5 school in the ", schoolConference])
                print(status)
            else:
                new_school = School(isPowerFive=0, name=schoolNameText)
                status = ''.join([schoolNameText, " is not a Power 5 school, they're in the ", schoolConference])
                print(status)
    
            session.add(new_school)
    
    session.commit()
