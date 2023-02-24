from bs4 import BeautifulSoup
import requests
import json

def getStats(playerurl):
  url = playerurl + ".html"
# url = "https://www.basketball-reference.com/players/b/bookede01.html"
  # this is the requests that is going to the url and bringing back the html
  result = requests.get(url)
  # print('text: ', result.text)
  # print('result: ', result)
  # this is just for parsing, i think you can ignore the following two lines
  doc = BeautifulSoup(result.text, "html.parser")
  # print('doc: ', doc)
  name = doc.select("#meta > div:nth-child(2) > h1 > span")
  statsDict = {}
  table = doc.select('#per_game > tbody')[0]
  rows = table.find_all('tr')

  # print('rows: ', rows)

  for i, row in enumerate(rows):
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
    # dealing with players that have season's missed due to injury
    # print('row length: ', len(row))
    #  normal season returns a len(row of 30)
    if len(row) < 30:
      # print('lees than')
      #this is an injured season and we want to add it differently
      info = row.find_all('td')
      # print('info: ', info[1].string)
      buildDict["age"] = info[1].string
      buildDict["miss_reason"] = info[2].string.encode("ascii", "ignore").decode()
      tmpyr = info[0].string
      year = year.join(tmpyr.split("-"))
      # print('year: ', year)
      # if year not in statsDict:
      #   statsDict[year] = [ buildDict ]
      # else:
      #   statsDict[year].append(buildDict)
      # statsDict[info[0].string] = buildDict
    else:
      # print('more than')
      stats = row.find_all("td")
      for stat in stats:
      # print('desc: ', stat['data-stat'], 'stat: ', stat.string)
        buildDict[stat['data-stat']] = stat.string
        # year = row.th.a.string
      year = (year).join(row.th.a.string.split("-"))
      # print('year: ', year)
      # statsDict[year] = buildDict
    # print('year before add: ', year)
    if year not in statsDict:
      statsDict[year] = [ buildDict ]
    else:
      statsDict[year].append(buildDict)

    #  the code below works when the playe has no injury seasons
    '''
    year = row.th.a.string
    year = ("_").join(year.split("-"))
    # grab all of the td elements
    statObj = {}
    stats = row.find_all("td")

    # print('stat 1: ', stats[0]['data-stat'])
    #below is working code that may need to be moved to if statement
    for stat in stats:
      # print('desc: ', stat['data-stat'], 'stat: ', stat.string)
      statObj[stat['data-stat']] = stat.string
      statsDict[year] = statObj

    '''
    # edit the year to remove dash

    # print('statObj: ', statObj)
  print('dict: ', json.dumps(statsDict, sort_keys=True, indent=4))
# getStats('https://www.basketball-reference.com/players/b/bookede01')
# getStats('https://www.basketball-reference.com/players/s/simmobe01')
getStats('https://www.basketball-reference.com/players/b/bridgmi01')

#per_game > tbody