from bs4 import BeautifulSoup
import requests
import asyncio

def getStats(playerurl):
  url = playerurl + ".html"
# url = "https://www.basketball-reference.com/players/b/bookede01.html"
  # this is the requests that is going to the url and bringing back the html
  result = requests.get(url)
  # print('result: ', result)
  # this is just for parsing, i think you can ignore the following two lines
  doc = BeautifulSoup(result.text, "html.parser")
  # print('doc: ', doc)
  name = doc.select("#meta > div:nth-child(2) > h1 > span")
  table = doc.select('#per_game > tbody')[0]
  rows = table.find_all('tr')

  print('table: ', rows)

getStats('https://www.basketball-reference.com/players/b/bookede01')

#per_game > tbody