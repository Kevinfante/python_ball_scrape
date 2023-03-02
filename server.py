from flask import Flask, jsonify, request
import roster
import stats
import careerStats
import util

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/roster/<string:team>', methods = ['GET'])
# get the current roster for a team by passing in their team code
def grabRoster(team):
  # check if there is an inputed older year
  year = request.args.get('year', util.getCurrYear())
  # let's take out roster and grab our roster using web scraping
  rosterData = roster.getRoster(team, year)
  # print(f'rosterData: {rosterData}')
  if len(rosterData):
    return jsonify(rosterData)
  else:
     return jsonify(rosterData), 404

@app.route('/stats/<string:team>/<string:number>', methods=['GET'])
# get the stats for a player by passing in their team code and current number
def getCurrStats(team,number):
  # let's see if the user want's to see the career averages, else default to false
  career = request.args.get('career', False)
  #first let's get the roster so that we can get the link
  rosterData = roster.getRoster(team)
  if number not in rosterData:
    return jsonify({}), 404
  if career:
    data = careerStats.getCareerStats(rosterData[number]['link'])
  else:
    data = stats.getStats(rosterData[number]['link'])
  # jsonify will return a status code of 200 by default
  return jsonify(data)

# @app.route('/stats/<string:team>/<int:number>/career', methods=["GET"])
# #def get career averages for a player by passing in their current team code and current number
# def getCareer(team, number):
#   rosterData = roster.getRoster(team)
#   number = str(number)
#   # need to put number as string for propper finding
#   if number not in rosterData:
#     return jsonify({}), 404
#   data = careerStats.getCareerStats(rosterData[number]['link'])
#   return jsonify(data)

if __name__ == "__main__":
    app.run(debug = True, host = "localhost", port = 8000)
