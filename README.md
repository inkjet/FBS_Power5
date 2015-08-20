#Python + College Football ![xx](http://i.imgur.com/YLw9efKt.png)
####Determing when large schools teams play small schools on the road

In college football scheduling, the Power 5 conference schools (ACC, Big Ten, Big 12, Pac-12, or SEC) almost always host schools from the smaller conferences (C-USA, MAC, etc).  The smaller school walks away with a paycheck of up to $1 million and the big school gets a win (usually).  

But occasionally a Power 5 school plays a small school on the road [for various reasons](http://espn.go.com/blog/acc/post/_/id/74265/acc-hits-the-road-vs-group-of-5), which is pretty cool. I wanted to know if and when these games happen, so I made a Python script to find out.

Requirements: 

+ Python 2.7 or 3.x
+ SQLAlchemy 0.9.4+
+ Beautiful Soup 4.3+

Note: both SQLAlchemy (for database creation) and Beautiful Soup (for web scraping) can be installed by `pip install sqlalchemy beautifulsoup4` or are available as pre-installed modules in [Anaconda](https://store.continuum.io/cshop/anaconda/).  

To run:

```
python print_results.py
```

The script first creates a blank MySQL database. Next, that database is populated with all FBS schools and their conference.  We scrape the [Wikipedia table](http://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_programs) of FBS schools.

Finally, we use that database with an online college football schedule to determine which Power 5 teams are playing road games vs. a non-Power 5 opponent each week.  I used the schedule on the [CBS Sports website](http://www.cbssports.com/collegefootball/schedules/FBS/week1).

Output for the 2015 season looks like this:

```
School database created at /home/user/FBS_Power5/FBS_schools.db

Air Force is not a Power 5 school, they're in the Mountain West
Akron is not a Power 5 school, they're in the MAC
Alabama is a Power 5 school in the SEC
<etc...>

Power 5 college football teams playing non-Power 5 teams on the road in 2015:

Week 1:
Oklahoma State at Central Michigan
Duke at Tulane
Baylor at SMU
Michigan State at Western Michigan
Washington at Boise State
Penn State at Temple
Mississippi State at Southern Miss
Purdue at Marshall
 
Week 2:
Minnesota at Colorado State
Pittsburgh at Akron
Missouri at Arkansas State
Arizona at Nevada
UCLA at UNLV
 
Week 3:
Colorado at Colorado State
NC State at Old Dominion
Iowa State at Toledo
Utah at Fresno State
 
Week 4:
Virginia Tech at East Carolina
NC State at South Alabama
 
Week 5:
 
Week 6:
Syracuse at South Florida
 
Week 7:
Ole Miss at Memphis
 
Week 8:
 
Week 9:
Vanderbilt at Houston
Notre Dame at Temple
 
Week 10:
 
Week 11:
 
Week 12:
 
Week 13:
 
Week 14:



```

