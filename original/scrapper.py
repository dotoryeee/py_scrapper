#StackOverflow Jobs
import requests
from bs4 import BeautifulSoup

def getLastPage(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find('div', {'class' : 's-pagination'}).find_all('a')
    last_page = pages[-2].span.get_text(strip=True)
    #return int(last_page)
    #테스트를 위해 2 페이지만 스크랩
    return 2

def extractJobs(URL, last_page):
    jobs = []
    for page in range(last_page):
        print(f'StackOverflow : scrapping {page+1}page')
        result = requests.get(f'{URL}&pg={page + 1}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div',{'class' : '-job'})
        for result in results:
            job = extractJob(result)
            jobs.append(job)
    return jobs

def extractJob(jobs):
    job_id = jobs['data-jobid']
    title = jobs.find('h2').a.string
    h3 = jobs.find('h3').find_all('span')
    for i, data in enumerate(h3):
        if i == 0:
            company = data.get_text(strip = True)#.string.strip()
        else:
            location = data.string.strip()
    return{'title':title,
           'company':company,
           'location':location,
           'link':f'https://stackoverflow.com/jobs/{job_id}'}

def scrapJobs(word):
    URL = f'https://stackoverflow.com/jobs?q={word}'
    last_page = getLastPage(URL)
    jobs = extractJobs(URL, last_page)
    return jobs