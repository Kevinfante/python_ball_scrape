from bs4 import BeautifulSoup
import requests
import json
from unidecode import unidecode
import util


def getRoster(team, year = util.getCurrYear()):
  url = f'https://www.basketball-reference.com/teams/{team.upper()}/{year}.html'

  result = requests.get(url)

  # deal with an page that is not there
  if result.status_code == 404:
    # print(f'result: {result.text}')
    return {}

  doc = BeautifulSoup(result.text, 'html.parser')

  roster = {'unregistered' : []}
  team_name = doc.select('#meta > div:nth-child(2) > h1:nth-child(1) > span:nth-child(2)')
  # roster[team] = team_name[0].string
  print('here i am')
  print(f'team: {team_name}')
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