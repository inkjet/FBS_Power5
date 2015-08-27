# -*- coding: utf-8 -*-
"""
Prints out the Power 5 vs. Non-Power 5 road matchups

Project page: https://github.com/inkjet/FBS_Power5

Author: Scott Rodkey, rodkeyscott@gmail.com

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bs4 import BeautifulSoup

from create_database import School
from scrape_websites import get_page

def calc_matchups(db_location):

    # Load the database
    engine = create_engine(db_location)
    School.metadata.bind = engine
    DBSession = sessionmaker()
    session = DBSession()

     # scrape the schedule from CBS since their site the easiest
    base_url = "http://www.cbssports.com/collegefootball/schedules/FBS/week"

    print(" ")
    print("----------")
    print(" ")
    print("Power 5 college football teams playing non-Power 5 teams on the road in 2015:")

    for week in range(14):

        print(" ")
        print("Week %d:" % (week+1))

        url = base_url + str(week+1)

        page = get_page(url)

        soup = BeautifulSoup(page.read(), "html.parser")

        table = soup.find_all("table", {"class" : "data"})

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
                    if a[-3:] == 'St.':
                        a = a[:-3] + "State"
                    if b[-3:] == 'St.':
                        b = b[:-3] + "State"

                    # Directional Michigans need to be expanded
                    if a[:2] == 'E.':
                        a = "".join(("Eastern", a[2:]))
                    if a[:2] == 'C.':
                        a = "".join(("Central", a[2:]))
                    if a[:2] == 'W.':
                        a = "".join(("Western", a[2:]))

                    # Change Miami "Fla." to "FL"
                    if b[-6:] == '(Fla.)':
                        b = 'Miami (FL)'
                        
                    # Various cleanups to reconcile between Wikipedia and CBS Sports
                    if a == 'M. Tenn. State':
                        a = 'Middle Tennessee'
                    if a == 'Texas-San Antonio':
                        a = 'UTSA'
                    if a == 'FAU':
                        a = 'Florida Atlantic'                      
                    if a == 'Army West Point':
                        a = 'Army'

                    home_check = session.query(School).filter(School.name == a).first()
                    away_check = session.query(School).filter(School.name == b).first()

                    if home_check and not home_check.isPowerFive and away_check and away_check.isPowerFive:
                        status = ''.join([b, " at ", a])
                        print(status)
