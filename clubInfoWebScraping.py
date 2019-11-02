import os, bs4, requests
import pandas as pd

PATH = "/Users/angli/Documents/GitHub/ClubPenguin2.0"
res = pd.DataFrame()
url = "https://activities.osu.edu/involvement/student_organizations/find_a_student_org/?page=0&l=ALL&c=Columbus"
findPageNum = "?page="
currPage = 0

#gets the next page of the list of activities
def next_page(soup):
    currPage += 1
    split = url.find(findPageNum + len(findPageNum))
    return url[0:split] + currPage + url[split+1:]

    while True:
        page = requests.get(url)
        res.to_csv(os.path.join(os.path.join(PATH,"clubInfo.csv")), index=None, sep=';', encoding='UTF-8')
        url = next_page(soup)

if __name__ == "__main__":
    main()

def main():
    page = requests.get(url)

    #on the first page, find the total number of pages
    if currPage == 0:
        soup = bs4.BeautifulSoup(page.content, 'lxml')
        numberOfPages = soup.find(name='span', attrs={'id':'tableID'})
