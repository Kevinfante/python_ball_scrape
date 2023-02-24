from bs4 import BeautifulSoup
import requests
import json
from unidecode import unidecode

def getRoster(team, year = 2023):
  url = f'https://www.basketball-reference.com/teams/{team.upper()}/{year}.html'

  result = requests.get(url)

  # deal with an page that is not there
  if result.status_code == 404:
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

# getRoster('lal',1985)