import os, bs4, requests
import pandas as pd

def table_to_df(table): 
  return pd.DataFrame([[td.text for td in row.findAll('td')] for row in table.tbody.findAll('tr')])

def next_page(soup): 
  return "http:" + soup.find('a', attrs={'rel':'next'}).get('href')

def main():
    PATH = os.path.join("C:\\","Users","Documents","OSU","HackOhio2019") # you need to change to your local path
    res = pd.DataFrame()
    url = "http://bank-code.net/country/FRANCE-%28FR%29/"
    counter = 0
    while True:
        if counter == 3:
            break
        print(counter)
        page = requests.get(url)
        soup = bs4.BeautifulSoup(page.content, 'lxml')
        table = soup.find(name='table', attrs={'id':'tableID'})
        if table is None:
            print("no table 'tableID' found for url {}".format(url))
            #print("html content:\n{}\n".format( page.content))
            #counter += 1
        else:
            res = res.append(table_to_df(table))
            res.to_csv(os.path.join(os.path.join(PATH,"clubInfo.csv")), index=None, sep=';', encoding='UTF-8')
            url = next_page(soup)
        counter += 1

if __name__ == "__main__":
    main()
