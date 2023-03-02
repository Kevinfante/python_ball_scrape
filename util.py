
from team_history import teams

# TODO: calculate what year to use based on when the website creates a new season roster

def getCurrYear():
    return 2023

def validate_year(team, year):
    if type(year) == str:
        year = int(year)
    # grab the object for years for the current team
    team_years = teams[team]
    # itearte over the keys until you find one in which the input year fits
    for key in team_years.keys():
        keys_arr = key.split("-")
        min = int(keys_arr[0])
        max = int(keys_arr[1])
        if min <= int(year) and max >= int(year):
            # the year was found, let's return the correct team code for that year
            return team_years[key]
    # if we never found a range in which the input year fits, then the input year is not valid
    return False

def validate_team_code(team):
    if team in teams:
        return team
    return False