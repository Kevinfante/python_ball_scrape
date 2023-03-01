from flask import Flask
from flask import Response
import roster
import stats
import careerStats
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/roster/<string:team>')
def grabRoster(team):
    # let's take out roster and grab our roster using web scraping
  rosterData = roster.getRoster(team)
  # print(f'rosterData: {rosterData}')
  rosterData = json.dumps(rosterData)

  print(f'length: {len(rosterData)}')

  if len(rosterData) > 3:
    return Response(rosterData, status=200, mimetype='application/json')
  else:
     return Response(rosterData, status=404)

@app.route('/stats/<string:team>/<int:number>')
#first let's get the roster so that we can get the link
def getCurrStats(team,number):
  rosterData = roster.getRoster(team)
  number = str(number)
  # need to put number as string for propper finding
  if number not in rosterData:
    return Response({}, status=404)
  data = stats.getStats(rosterData[number]['link'])
  data = json.dumps(data)
  return Response(data, status = 200)

@app.route('/stats/<string:team>/<int:number>/career')
#def get career Stats for a player
def getCareer(team, number):
   return 'exit'