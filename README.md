FBS_Power5
==========

In the world of college football, the big-money schools will pay smaller schools to come play at their stadium.  The smaller school walks away with a paycheck of up to $1 million for agreeing to the game, and the big school gets a win (usually).  

But occaisionally a big name school plays a smaller school on the road [for various reasons](http://espn.go.com/blog/acc/post/_/id/74265/acc-hits-the-road-vs-group-of-5), and I love watching those games.  It's a huge game for the smaller school, and the bigger Power 5 school just wants to escape with a win.  

I wanted to know if and when these games happen each week, so I made a Python script to determine when a college football team from a Power 5 conference (ACC, Big Ten, Big 12, Pac-12, or SEC) plays a non-power 5 school on the road.

Requirements: 

+ Python 2.7
+ SQLAlchemy 0.9.4+
+ Beautiful Soup 4.3+

Both SQLAlchemy (for database creation) and Beautiful Soup (for web scraping) are available as pre-installed modules in [Anaconda](https://store.continuum.io/cshop/anaconda/).  

Running this is a three-step process.  First, create an empty database:

```python
python create_database.py
```

Next, populate that database with all FBS schools and their conference.  This scrapes the [Wikipedia table](http://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_programs) that lists all FBS schools.

```python
populate_db.py
```

Finally, use that database and a schedule to determine which Power 5 teams are playing road games vs. a non-Power 5 opponent each week.  I found the weekly schedule on the [CBS Sports website](http://www.cbssports.com/collegefootball/schedules/FBS/week1) was the easiest to scrape.

```python
python calc_matchups.py
```

Below is the full output. Feel free to play with the calc_matchups.py file to determine other interesting weekly matchups.

The full output for the 2014 season looks like this:

```
Week 1:
Penn State at UCF
Ohio State at Navy
Boston College at Massachusetts
 
Week 2:
Washington State at Nevada
Missouri at Toledo
Oklahoma at Tulsa
Colorado at Massachusetts
Maryland at South Florida
Georgia Tech at Tulane
Duke at Troy
Arizona State at New Mexico
Michigan at Notre Dame
Texas Tech at UTEP
 
Week 3:
Baylor at Buffalo
Pittsburgh at FIU
Indiana at Bowling Green
Mississippi State at South Alabama
Wake Forest at Utah State
Purdue at Notre Dame
Nebraska at Fresno State
 
Week 4:
Rutgers at Navy
Louisville at FIU
Texas A&M at SMU
North Carolina at East Carolina
Virginia at BYU
 
Week 5:
TCU at SMU
 
Week 6:
Stanford at Notre Dame
 
Week 7:
North Carolina at Notre Dame
 
Week 8:
 
Week 9:
 
Week 10:
 
Week 11:
 
Week 12:
Northwestern at Notre Dame
 
Week 13:
Louisville at Notre Dame
```

