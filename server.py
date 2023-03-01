from flask import Flask, jsonify
import roster
import stats
import careerStats

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/roster/<string:team>')
def grabRoster(team):
    # let's take out roster and grab our roster using web scraping
  rosterData = roster.getRoster(team)

  if len(rosterData):
    return jsonify(rosterData)
  else:
     return jsonify(rosterData), 404

@app.route('/stats/<string:team>/<int:number>')
#first let's get the roster so that we can get the link
def getCurrStats(team,number):
  rosterData = roster.getRoster(team)
  number = str(number)
  # need to put number as string for propper finding
  if number not in rosterData:
    return jsonify({}), 404
  data = stats.getStats(rosterData[number]['link'])
  # jsonify will return a status code of 200 by default
  return jsonify(data)

@app.route('/stats/<string:team>/<int:number>/career')
#def get career averages for a player
def getCareer(team, number):
  rosterData = roster.getRoster(team)
  number = str(number)
  # need to put number as string for propper finding
  if number not in rosterData:
    return jsonify({}), 404
  data = careerStats.getCareerStats(rosterData[number]['link'])
  # data = json.dumps(data, indent=4, sort_keys=True)
  return jsonify(data)

if __name__ == "__main__":
    app.run(debug = True, host = "localhost", port = 8000)