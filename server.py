from flask import Flask, jsonify, request
import util
from data import getCareerStats, getRoster, getStats
from decorators import exception_handler

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/roster/<string:team>', methods = ['GET'])
# get the current roster for a team by passing in their team code
@exception_handler
def grabRoster(team):
  # check if there is an inputed older year
  year = request.args.get('year', util.getCurrYear())
  # let's take out roster and grab our roster using web scraping
  rosterData = getRoster(team, year)
  if len(rosterData):
    return jsonify(rosterData)
  else:
     return jsonify(rosterData), 404

@app.route('/stats/<string:team>/<string:number>', methods=['GET'])
# get the stats for a player by passing in their team code and current number
def grabStats(team,number):
  # let's see if the user want's to see the career averages, else default to false
  career = request.args.get('career', False)
  #first let's get the roster so that we can get the link
  rosterData = getRoster(team)
  if number not in rosterData:
    return jsonify({}), 404
  if career:
    data = getCareerStats(rosterData[number]['link'])
  else:
    data = getStats(rosterData[number]['link'])
  # jsonify will return a status code of 200 by default
  return jsonify(data)

if __name__ == "__main__":
    app.run(debug = True, host = "localhost", port = 8000)
