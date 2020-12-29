#Indeed Jobs
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://kr.indeed.com/jobs?q=%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C&limit={LIMIT}'

def getLastPage():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div',{'class' : 'pagination'})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    last_page = pages[-1]
    #return last_page
    #테스트를 위해 2 페이지만 스크랩
    return 2

def getJobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'INDEED : scrapping {page+1}page')
        result = requests.get(f'{URL}&start={page * LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div',{'class' : 'jobsearch-SerpJobCard'})
        for result in results:
            job = extractJobs(result)
            jobs.append(job)
    return jobs

def extractJobs(html):
    title = html.find('h2', {'class': 'title'}).find('a')['title']
    jobID = html.find('a')['id'].strip('jl_')
    company = html.find('span',{'class': 'company'})
    companyAnchor = company.find('a')
    location = html.find('span', {'class': 'location'}).string
    if companyAnchor != None:
        company = company.find('a').string.strip()#strip:리턴문자 삭제
    else:
        company = company.string.strip()
    return{'title':title,
           'company':company,
           'location':location,
           'link':f'https://kr.indeed.com/viewjob?jk={jobID}'}

def scrapJobs():
    lastPage = getLastPage()
    jobs = getJobs(lastPage)
    return jobs

