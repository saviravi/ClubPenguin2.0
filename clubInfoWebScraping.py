import os, bs4, requests
import pandas as pd

PATH = os.path.join("C:\\","Users","xxx","Documents","py") # you need to change to your local path
res = pd.DataFrame()
url = "http://bank-code.net/country/FRANCE-%28FR%29/"
counter = 0

def table_to_df(table): 
  return pd.DataFrame([[td.text for td in row.findAll('td')] for row in table.tbody.findAll('tr')])

def next_page(soup): 
  return "http:" + soup.find('a', attrs={'rel':'next'}).get('href')

while True:
  print(counter)
  page = requests.get(url)
  soup = bs4.BeautifulSoup(page.content, 'lxml')
  table = soup.find(name='table', attrs={'id':'tableID'})
  res = res.append(table_to_df(table))
  res.to_csv(os.path.join(os.path.join(PATH,"table.csv")), index=None, sep=';', encoding='iso-8859–1')
  url = next_page(soup)
  counter += 1
