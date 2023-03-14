# BasketBall Ref Scraper
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Overview
This is a flask project that scrapes basketball reference to give users NBA roster and player data

## Setup
1. Clone down this repo.
1. Create a virtual enviornment to prevent any errors due to dependencies.
 1. Steps to create virtual enviornment:
    1. Make sure that python3 is installed on your device and navigate to the directory where the project is located
    1. Once in the desired directory, run ``python3 -m {virtual env name} .{virtual env name}``  for example: `` python3 -m env .env`` to create the virtual enviornment
    1. Activate the virtual enviornment by running `` . .{virtual env name}/bin/activate `` For Example: `` . .env/bin/activate ``
1. After the virtualenv is running, install dependincies with ``pip install -r requirements.txt``.
1. start the server with ``python server.py``.
1. the server will now be running on localhost:8000

## Endpoints

### Get Roster
| HTTP Request | Endpoint | Description |
|--------------|-----------|-------------|
| GET | `` /roster/:team `` | Returns a dictionary players and general player info in the roster with their jersey number as a key|

 #### Parameters
 | Parameter | Type | Description |
 |-----------|------|-------------|
 | team | String | A Code for each Team (see Team Codes table for valid codes) |

 #### Get Params
 | Parameter | Type | Description |
 |-----------|------|-------------|
 | year | Int | The year of the roster that we are interested in seeing |


#### Team Codes

 | Team Codes | Type | Team |
 |-----------|------|-------------|
 | ATL | String | Atlanta Hawks |
 | BOS | String | Boston Celtics |
 | BRK | String | Brooklyn Nets |
 | CHO | String | Charlotte Hornets |
 | CHI | String | Chicago Bulls |
 | CLE | String | Cleveland Cavaliers |
 | DAL | String | Dallas Mavericks |
 | DEN | String | Denver Nuggets |
 | DET | String | Detroit Pistons |
 | GSW | String | Golden State Warriors |
 | HOU | String | Houston Rockets |
 | IND | String | Indiana Pacers |
 | LAC | String | Los Angeles Clippers |
 | LAL | String | Los Angeles Lakers |
 | MEM | String | Memphis Grizzlies |
 | MIA | String | Miami Heat |
 | MIL | String | Milwaukee Bucks |
 | MIN | String | Minnesotta Timberwolves |
 | NOP | String | New Orleans Pelicans |
 | NYK | String | New York Knicks |
 | OKC | String | Oklahoma City Thunder |
 | ORL | String | Orlando Magic |
 | PHI | String | Philedelphia 76ers |
 | PHO | String | Phoenix Suns |
 | POR | String | Portland Trailblazers |
 | SAC | String | Sacramento Kings |
 | SAS | String | San Antonio Spurs |
 | TOR | String | Toronto Raptors |
 | UTA | String | Utah Jazz |
 | WAS | String | Washington Celtics |
 | BOS | String | Boston Celtics |

#### Example
  #### Request: `` /roster/LAL ``
  #### Response:
  ```
  {
    "Team" : "Los Angeles Lakers",
    "1": {
        "birth_country": "us",
        "birth_date": "February 23, 1996",
        "college": "Ohio State",
        "height": "6-4",
        "link": "/players/r/russeda01",
        "player": "Russell,D'Angelo",
        "pos": "PG",
        "weight": "193",
        "years_experience": "7"
    },
    "10": {
        "birth_country": "us",
        "birth_date": "February 10, 2003",
        "college": "Michigan State",
        "height": "6-6",
        "link": "/players/c/chrisma02",
        "player": "Christie,Max",
        "pos": "SG",
        "weight": "190",
        "years_experience": "R"
    },
    "11": {
        "birth_country": "us",
        "birth_date": "June 11, 1995",
        "college": "Miami (FL)",
        "height": "6-5",
        "link": "/players/r/reedda01",
        "player": "Reed,Davon",
        "pos": "SG",
        "weight": "208",
        "years_experience": "3"
    },
    "12": {
        "birth_country": "us",
        "birth_date": "May 12, 1998",
        "college": "Texas",
        "height": "7-0",
        "link": "/players/b/bambamo01",
        "player": "Bamba,Mohamed",
        "pos": "C",
        "weight": "231",
        "years_experience": "4"
    },
    "14": {
        "birth_country": "us",
        "birth_date": "November 10, 2000",
        "college": "Vanderbilt",
        "height": "6-3",
        "link": "/players/p/pippesc02",
        "player": "Pippen ,Scotty",
        "pos": "PG",
        "weight": "185",
        "years_experience": "R"
    },
    "15": {
        "birth_country": "us",
        "birth_date": "May 29, 1998",
        "college": null,
        "height": "6-5",
        "link": "/players/r/reaveau01",
        "player": "Reaves,Austin",
        "pos": "SG",
        "weight": "206",
        "years_experience": "1"
    },
    "17": {
        "birth_country": "de",
        "birth_date": "September 15, 1993",
        "college": null,
        "height": "6-3",
        "link": "/players/s/schrode01",
        "player": "Schroder,Dennis",
        "pos": "PG",
        "weight": "172",
        "years_experience": "9"
    },
    "2": {
        "birth_country": "us",
        "birth_date": "April 3, 1999",
        "college": "Kentucky",
        "height": "6-9",
        "link": "/players/v/vandeja01",
        "player": "Vanderbilt,Jarred",
        "pos": "PF",
        "weight": "214",
        "years_experience": "4"
    },
    "20": {
        "birth_country": "us",
        "birth_date": "May 8, 1999",
        "college": null,
        "height": "6-9",
        "link": "/players/s/swideco01",
        "player": "Swider,Cole",
        "pos": "SF",
        "weight": "220",
        "years_experience": "R"
    },
    "28": {
        "birth_country": "jp",
        "birth_date": "February 8, 1998",
        "college": "Gonzaga",
        "height": "6-8",
        "link": "/players/h/hachiru01",
        "player": "Hachimura,Rui",
        "pos": "PF",
        "weight": "230",
        "years_experience": "3"
    },
    "3": {
        "birth_country": "us",
        "birth_date": "March 11, 1993",
        "college": "Kentucky",
        "height": "6-10",
        "link": "/players/d/davisan02",
        "player": "Davis,Anthony",
        "pos": "C",
        "weight": "253",
        "years_experience": "10"
    },
    "35": {
        "birth_country": "sd",
        "birth_date": "March 26, 1997",
        "college": "Kentucky",
        "height": "6-9",
        "link": "/players/g/gabriwe01",
        "player": "Gabriel,Wenyen",
        "pos": "PF",
        "weight": "205",
        "years_experience": "3"
    },
    "4": {
        "birth_country": "us",
        "birth_date": "December 14, 1998",
        "college": "Miami (FL)",
        "height": "6-4",
        "link": "/players/w/walkelo01",
        "player": "Walker,Lonnie",
        "pos": "SG",
        "weight": "204",
        "years_experience": "4"
    },
    "5": {
        "birth_country": "us",
        "birth_date": "November 26, 1996",
        "college": "Florida State",
        "height": "6-4",
        "link": "/players/b/beaslma01",
        "player": "Beasley,Malik",
        "pos": "SG",
        "weight": "187",
        "years_experience": "6"
    },
    "6": {
        "birth_country": "us",
        "birth_date": "December 30, 1984",
        "college": null,
        "height": "6-9",
        "link": "/players/j/jamesle01",
        "player": "James,LeBron",
        "pos": "PF",
        "weight": "250",
        "years_experience": "19"
    },
    "7": {
        "birth_country": "us",
        "birth_date": "July 28, 1999",
        "college": "Oregon",
        "height": "6-6",
        "link": "/players/b/browntr01",
        "player": "Brown,Troy",
        "pos": "SF",
        "weight": "215",
        "years_experience": "4"
    }
}
```

  #### Reqests: ``/roster/LAL?year=1998``
  #### Response:
  ```
   {
    "Team": "Los Angeles Lakers",
    "17": {
        "birth_country": "ca",
        "birth_date": "July 24, 1969",
        "college": "UNC",
        "height": "6-7",
        "link": "/players/f/foxri01",
        "player": "Fox,Rick",
        "pos": "SF",
        "weight": "230",
        "years_experience": "6"
    },
    "2": {
        "birth_country": "us",
        "birth_date": "August 9, 1974",
        "college": "Little Rock",
        "height": "6-1",
        "link": "/players/f/fishede01",
        "player": "Fisher,Derek",
        "pos": "PG",
        "weight": "200",
        "years_experience": "1"
    },
    "20": {
        "birth_country": "us",
        "birth_date": "July 25, 1969",
        "college": null,
        "height": "6-4",
        "link": "/players/b/barryjo01",
        "player": "Barry,Jon",
        "pos": "SG",
        "weight": "195",
        "years_experience": "5"
    },
    "23": {
        "birth_country": "us",
        "birth_date": "August 1, 1973",
        "college": "Arizona State",
        "height": "6-6",
        "link": "/players/b/bennema01",
        "player": "Bennett,Mario",
        "pos": "PF",
        "weight": "235",
        "years_experience": "1"
    },
    "24": {
        "birth_country": "us",
        "birth_date": "August 26, 1975",
        "college": "Tulsa",
        "height": "6-5",
        "link": "/players/s/sealssh01",
        "player": "Seals,Shea",
        "pos": "SG",
        "weight": "210",
        "years_experience": "R"
    },
    "34": {
        "birth_country": "us",
        "birth_date": "March 6, 1972",
        "college": "LSU",
        "height": "7-1",
        "link": "/players/o/onealsh01",
        "player": "O'Neal,Shaquille",
        "pos": "C",
        "weight": "325",
        "years_experience": "5"
    },
    "41": {
        "birth_country": "us",
        "birth_date": "July 23, 1968",
        "college": "Clemson",
        "height": "6-11",
        "link": "/players/c/campbel01",
        "player": "Campbell,Elden",
        "pos": "PF",
        "weight": "215",
        "years_experience": "7"
    },
    "43": {
        "birth_country": "us",
        "birth_date": "January 4, 1969",
        "college": "Cincinnati",
        "height": "6-9",
        "link": "/players/b/blounco01",
        "player": "Blount,Corie",
        "pos": "PF",
        "weight": "240",
        "years_experience": "4"
    },
    "45": {
        "birth_country": "us",
        "birth_date": "September 9, 1969",
        "college": "Arizona",
        "height": "6-10",
        "link": "/players/r/rooksse01",
        "player": "Rooks,Sean",
        "pos": "C",
        "weight": "250",
        "years_experience": "5"
    },
    "5": {
        "birth_country": "us",
        "birth_date": "August 25, 1970",
        "college": "Alabama",
        "height": "6-10",
        "link": "/players/h/horryro01",
        "player": "Horry,Robert",
        "pos": "PF",
        "weight": "240",
        "years_experience": "5"
    },
    "6": {
        "birth_country": "us",
        "birth_date": "October 20, 1971",
        "college": "Temple",
        "height": "6-6",
        "link": "/players/j/jonesed02",
        "player": "Jones,Eddie",
        "pos": "SG",
        "weight": "190",
        "years_experience": "3"
    },
    "8": {
        "birth_country": "us",
        "birth_date": "August 23, 1978",
        "college": null,
        "height": "6-6",
        "link": "/players/b/bryanko01",
        "player": "Bryant,Kobe",
        "pos": "SF",
        "weight": "212",
        "years_experience": "1"
    },
    "9": {
        "birth_country": "us",
        "birth_date": "November 27, 1971",
        "college": null,
        "height": "6-1",
        "link": "/players/v/vanexni01",
        "player": "Van Exel,Nick",
        "pos": "PG",
        "weight": "170",
        "years_experience": "4"
    }
}
```

#### NOTE: IF a player has not played or has not been assigned a jersey number for their team, they will not show up in the dictionary

### Get Stats
| HTTP Request | Endpoint | Description |
|--------------|-----------|-------------|
| GET | `` /stats/:team/:jersey_number `` | Returns a dictionary of stats seperated by seasons|

 #### Parameters
 | Parameter | Type | Description |
 |-----------|------|-------------|
 | team | String | A code for each team (see Team Codes table for valid codes) |
 | jersey_number | int | The desired players jersey number |

 #### Get Params
 | Parameter | Type | Description |
 |-----------|------|-------------|
 | career | boolean | default is false, but if passed true, will return career aveages for desired player |

#### Example
  #### Request: ``/stats/MEM/3 ``
  #### Response:
  ```
  {
    "name": "Ja Morant",
    "2019_20": [
        {
            "age": "20",
            "ast_per_g": "7.3",
            "blk_per_g": "0.3",
            "drb_per_g": "3.1",
            "efg_pct": ".509",
            "fg2_pct": ".511",
            "fg2_per_g": "5.8",
            "fg2a_per_g": "11.3",
            "fg3_pct": ".335",
            "fg3_per_g": "0.9",
            "fg3a_per_g": "2.7",
            "fg_pct": ".477",
            "fg_per_g": "6.7",
            "fga_per_g": "14.0",
            "ft_pct": ".776",
            "ft_per_g": "3.6",
            "fta_per_g": "4.6",
            "g": "67",
            "gs": "67",
            "lg_id": "NBA",
            "miss_reason": "N/A",
            "mp_per_g": "31.0",
            "orb_per_g": "0.8",
            "pf_per_g": "1.6",
            "pos": "PG",
            "pts_per_g": "17.8",
            "stl_per_g": "0.9",
            "team_id": "MEM",
            "tov_per_g": "3.3",
            "trb_per_g": "3.9"
        }
    ],
    "2020_21": [
        {
            "age": "21",
            "ast_per_g": "7.4",
            "blk_per_g": "0.2",
            "drb_per_g": "3.1",
            "efg_pct": ".487",
            "fg2_pct": ".499",
            "fg2_per_g": "5.7",
            "fg2a_per_g": "11.4",
            "fg3_pct": ".303",
            "fg3_per_g": "1.2",
            "fg3a_per_g": "3.8",
            "fg_pct": ".449",
            "fg_per_g": "6.8",
            "fga_per_g": "15.2",
            "ft_pct": ".728",
            "ft_per_g": "4.3",
            "fta_per_g": "5.9",
            "g": "63",
            "gs": "63",
            "lg_id": "NBA",
            "miss_reason": "N/A",
            "mp_per_g": "32.6",
            "orb_per_g": "0.9",
            "pf_per_g": "1.4",
            "pos": "PG",
            "pts_per_g": "19.1",
            "stl_per_g": "0.9",
            "team_id": "MEM",
            "tov_per_g": "3.2",
            "trb_per_g": "4.0"
        }
    ],
    "2021_22": [
        {
            "age": "22",
            "ast_per_g": "6.7",
            "blk_per_g": "0.4",
            "drb_per_g": "4.4",
            "efg_pct": ".530",
            "fg2_pct": ".534",
            "fg2_per_g": "8.6",
            "fg2a_per_g": "16.2",
            "fg3_pct": ".344",
            "fg3_per_g": "1.5",
            "fg3a_per_g": "4.5",
            "fg_pct": ".493",
            "fg_per_g": "10.2",
            "fga_per_g": "20.6",
            "ft_pct": ".761",
            "ft_per_g": "5.5",
            "fta_per_g": "7.3",
            "g": "57",
            "gs": "57",
            "lg_id": "NBA",
            "miss_reason": "N/A",
            "mp_per_g": "33.1",
            "orb_per_g": "1.4",
            "pf_per_g": "1.5",
            "pos": "PG",
            "pts_per_g": "27.4",
            "stl_per_g": "1.2",
            "team_id": "MEM",
            "tov_per_g": "3.4",
            "trb_per_g": "5.7"
        }
    ],
    "2022_23": [
        {
            "age": "23",
            "ast_per_g": "8.2",
            "blk_per_g": "0.2",
            "drb_per_g": "4.8",
            "efg_pct": ".502",
            "fg2_pct": ".512",
            "fg2_per_g": "8.0",
            "fg2a_per_g": "15.6",
            "fg3_pct": ".316",
            "fg3_per_g": "1.6",
            "fg3a_per_g": "5.1",
            "fg_pct": ".463",
            "fg_per_g": "9.6",
            "fga_per_g": "20.6",
            "ft_pct": ".744",
            "ft_per_g": "6.4",
            "fta_per_g": "8.5",
            "g": "53",
            "gs": "53",
            "lg_id": "NBA",
            "miss_reason": "N/A",
            "mp_per_g": "32.5",
            "orb_per_g": "1.1",
            "pf_per_g": "1.7",
            "pos": "PG",
            "pts_per_g": "27.1",
            "stl_per_g": "1.1",
            "team_id": "MEM",
            "tov_per_g": "3.4",
            "trb_per_g": "6.0"
        }
    ]
}
```
#### NOTE: if a player was traded mid-season, that year will have multiple dictionaries in the List for that year, one for their stats during their time with each team and one for their total averages during the season