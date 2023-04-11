from flask import Flask, jsonify, request
import util
from data import getCareerStats, getRoster, getStats
from decorators import logger
# from decorators import Error_Handler

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/stats/<string:team>/<string:number>', methods=['GET'])
@logger
# get the stats for a player by passing in their team code and current number
def grabStats(team,number):
  # let's see if the user want's to see the career averages, else default to false
  career = request.args.get('career', False)
  #first let's get the roster so that we can get the link
  rosterData = getRoster(team)
  if number not in rosterData:
    raise ValueError("Can't seem to find that player, they may be unregistered, please check again.")
  if career:
    data = getCareerStats(rosterData[number]['link'])
  else:
    data = getStats(rosterData[number]['link'])
  # jsonify will return a status code of 200 by default
  return jsonify(data)


@app.route('/roster/<string:team>', methods = ['GET'])
# get the current roster for a team by passing in their team code
@logger
def grabRoster(team):
  # check if there is an inputed older year
  year = request.args.get('year', util.getCurrYear())
  if type(year) == str and not year.isnumeric():
    raise ValueError('please enter a valid year.')

  #  lets validate the input team code
  validate_team = util.validate_team_code(team.upper())
  if not validate_team:
    raise ValueError("please input a valid team code.")

  updated_team = util.validate_year(team, year)
  # check if the team code existed in the year and see if the code needs to be udpated
  if not updated_team:
    raise ValueError(f"please input a valid year for {team}")
  # let's take out roster and grab our roster using web scraping
  rosterData = getRoster(updated_team, year)
  if len(rosterData):
    return jsonify(rosterData)
  else:
    return jsonify({rosterData}), 404

if __name__ == "__main__":
    app.run(debug = True, host = "localhost", port = 8000)