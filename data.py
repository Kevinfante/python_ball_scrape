from bs4 import BeautifulSoup
import requests
from unidecode import unidecode
import util

# function returns a large dictionary breaking down a player's stats by year
def getStats(playerurl):
  url = f"https://www.basketball-reference.com{playerurl}.html"

  # this is the requests that is going to the url and bringing back the html
  result = requests.get(url)
  # deal with an page that is not there
  if result.status_code == 404:
    return {}

  # parse the html
  doc = BeautifulSoup(result.text, "html.parser")

  # grab the player name
  name = doc.select("#meta > div:nth-child(2) > h1 > span")
  # thie is the obj that will be returned
  statsDict = {}

  # select the 'tbody' that holds the table
  table = doc.select('#per_game > tbody')[0]
  rows = table.find_all('tr')

  for row in rows:
    # need to create the build dict here in
    buildDict = {
      'age': 'N/A',
      'team_id': 'N/A',
      'lg_id': 'N/A',
      'pos': 'N/A',
      'g': 'N/A',
      'gs': 'N/A',
      'mp_per_g': 'N/A',
      'fg_per_g': 'N/A',
      'fga_per_g': 'N/A',
      'fg_pct': 'N/A',
      'fg3_per_g': 'N/A',
      'fg3a_per_g': 'N/A',
      'fg3_pct': 'N/A',
      'fg2_per_g': 'N/A',
      'fg2a_per_g': 'N/A',
      'fg2_pct': 'N/A',
      'efg_pct': 'N/A',
      'ft_per_g': 'N/A',
      'fta_per_g': 'N/A',
      'ft_pct': 'N/A',
      'orb_per_g': 'N/A',
      'drb_per_g': 'N/A',
      'trb_per_g': 'N/A',
      'ast_per_g': 'N/A',
      'stl_per_g': 'N/A',
      'blk_per_g': 'N/A',
      'tov_per_g': 'N/A',
      'pf_per_g': 'N/A',
      'pts_per_g': 'N/A',
      'miss_reason': 'N/A'
      }
    year = "_"
    #  normal season returns a len(row of 30)
    if len(row) < 30:
      #this is an injured season and we want to add it differently
      info = row.find_all('td')
      buildDict["age"] = info[1].string
      buildDict["miss_reason"] = info[2].string.encode("ascii", "ignore").decode()
      tmpyr = info[0].string
      year = year.join(tmpyr.split("-"))

    else:
      stats = row.find_all("td")
      for stat in stats:
        buildDict[stat['data-stat']] = stat.string
      year = (year).join(row.th.a.string.split("-"))
    if year not in statsDict:
      statsDict[year] = [ buildDict ]
    else:
      statsDict[year].append(buildDict)

  # print('dict: ', json.dumps(statsDict, sort_keys=True, indent=4))
  return statsDict


# returns a dictionary of players with their jersey number as the key value
# unregisterd players are ignored as they do not currently have a jersey number
def getRoster(team, year = util.getCurrYear()):
  url = f'https://www.basketball-reference.com/teams/{team.upper()}/{year}.html'

  result = requests.get(url)

  # deal with an page that is not there
  if result.status_code == 404:
    # print(f'result: {result.text}')
    return {}

  doc = BeautifulSoup(result.text, 'html.parser')

  roster = {'unregistered' : []}

  rosterTable = doc.select('#roster > tbody')[0]
  players = rosterTable.find_all('tr')

  for player in players:
    # print('player: ', player.th.string)
    number = player.th.string
    infoObj = {}
    info = player.find_all("td")
    for det in info:
      if det['data-stat'] == 'player':
        name = unidecode(det['csk'])
        link = det.a['href']
        infoObj['player'] = name
        infoObj['link'] = link[:-5]
      else:
        infoObj[det['data-stat']] = det.string
    if number:
      roster[number] = infoObj
    else:
      roster['unregistered'].append(infoObj)
  # print(json.dumps(roster, sort_keys = True, indent = 4))
  return roster


# function returns a dict of career averages along with some aggregate values for a player
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