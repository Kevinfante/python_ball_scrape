from bs4 import BeautifulSoup
import requests
import asyncio

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
    # edit the year to remove dash
    year = row.th.a.string
    year = ("_").join(year.split("-"))
    # grab all of the td elements
    # statObj = {}
    stats = row.find_all("td")
    # print('stat 1: ', stats[0]['data-stat'])
    for stat in stats:
      print('desc: ', stat['data-stat'], 'stat: ', stat.string)

  #   print('i: ', i, 'find_all: ', row.fi)
    # print('i: ', i, 'row: ', row)
    # print('type: ', type(row), 'row: ', row)
  #   ex = BeautifulSoup(row, 'html.parser')
    # for stat in row.children:
      # print('stat: ', stat)
  # print('table: ', rows)

getStats('https://www.basketball-reference.com/players/b/bookede01')

#per_game > tbody