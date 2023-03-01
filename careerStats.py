from bs4 import BeautifulSoup
import requests
import json
from unidecode import unidecode

def getCareerStats(player):
  url = f"https://www.basketball-reference.com{player}.html"

  result = requests.get(url)
  # deal with an page that is not there
  if result.status_code == 404:
    return {}

  doc = BeautifulSoup(result.text, "html.parser")

  # find the player name
  name = doc.select("#meta > div:nth-child(2) > h1 > span")

  # find the career WS
  ws = doc.select("#info > div.stats_pullout > div.p3 > div:nth-child(2) > p:nth-child(3)")

  # find the career PER
  per = doc.select("#info > div.stats_pullout > div.p3 > div:nth-child(1) > p:nth-child(3)")


  statsDict = {}
  statsDict['player'] = unidecode(name[0].string)
  statsDict['win_shares'] = ws[0].string
  statsDict['per'] = per[0].string

  # find the career row in the table
  row = doc.select("#per_game > tfoot > tr:nth-child(1)")[0]
  stats = row.find_all("td")

  # empty stats
  ignore = set(['age', 'team_id', 'lg_id', 'pos'])

  for stat in stats:
    # some career stats are completely empty so we want to ignore those
    if stat['data-stat'] in ignore:
      continue
    statsDict[stat['data-stat']] = stat.string

  # print('statsDict: ', statsDict)
  # print('statsDict ', json.dumps(statsDict, sort_keys=True, indent=4))
  # print('dict: ', json.dumps(statsDict, sort_keys=True, indent=4))

  return statsDict

# getCareerStats('/players/d/doncilu01')