# -*- coding: utf-8 -*-
"""
Prints out the Power 5 vs. Non-Power 5 road matchups

First run create_database.py, then populate_db.py
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bs4 import BeautifulSoup
import urllib2
 
from create_database import School

def calc_matchups(db_location):

    # Load the database
    engine = create_engine(db_location)
    School.metadata.bind = engine 
    DBSession = sessionmaker()
    session = DBSession()
    
     # scrape the schedule from CBS since their site the easiest
    base_url="http://www.cbssports.com/collegefootball/schedules/FBS/week"
    
    for week in range(14):
        
        print(" ")
        print("Week %d:" % (week+1))
        
        url = base_url + str(week+1)
        
        page=urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())
        
        table = soup.find_all("table", { "class" : "data" })
         
        for x in table:
            for row in x.findAll("tr"):
                cells = row.findAll("td")
                matchup = cells[0].findAll(text=True)
                # format is "Team 1" vs. "Team 2", which will be a 3-item string array        
                if len(matchup) != 3:
                    pass
                else:
                    away_team = matchup[0]
                    home_team = matchup[2]
                    # convert home team to string
                    a = ''.join(home_team)
                    b = ''.join(away_team)
                    
                    # CBS lists state teams as "St.", while Wikipedia does it as "State"  Need to replace
                    if (a[-3:] == 'St.'):
                        a = a[:-3]
                        a = a + "State"
                    if (b[-3:] == 'St.'):
                        b = b[:-3]
                        b = b + "State"                
                    
                    home_check = session.query(School).filter(School.name == a).first()
                    away_check = session.query(School).filter(School.name == b).first()
                    if home_check is None or \
                       away_check is None:
                           pass
                    elif (home_check.isPowerFive == 0) and \
                       (away_check.isPowerFive == 1):
                           status = ''.join([b, " at ", a])
                           print(status)

                    
