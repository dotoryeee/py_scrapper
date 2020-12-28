#StackOverFlow Jobs
import requests
from bs4 import BeautifulSoup
print()

URL = 'https://stackoverflow.com/jobs?q=cloud'


def getLastPage():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class' : 's-pagination'}).find_all('a')
    print(pages)


def scrapJobs():
    last_page = getLastPage()
    return last_page