from bs4 import BeautifulSoup
import requests
# import json

def getStats(playerurl):
  url = playerurl + ".html"

  # this is the requests that is going to the url and bringing back the html
  result = requests.get(url)

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
    # need to create the build dict here in order to ensure return consistency
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
# getStats('https://www.basketball-reference.com/players/b/bookede01')
# getStats('https://www.basketball-reference.com/players/s/simmobe01')
# getStats('https://www.basketball-reference.com/players/b/bridgmi01')
