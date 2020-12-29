#StackOverFlow Jobs
import requests
from bs4 import BeautifulSoup

URL = 'https://stackoverflow.com/jobs?q=cloud'


def getLastPage():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class' : 's-pagination'}).find_all('a')
    last_page = pages[-2].span.get_text(strip = True)
    return int(last_page)

def extractJobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{URL}&pg={page + 1}')
        soup = BeautifulSoup(result.text, 'html.parser')
        jobs = soup.find('div', {'class' : 'listResults'}).find_all('div',{'class' : 'f11'})
        title = jobs.find

        print(jobs)



def scrapJobs():
    last_page = getLastPage()
    jobs = extractJobs(last_page)
    return jobs