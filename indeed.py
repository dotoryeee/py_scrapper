import requests
from bs4 import BeautifulSoup
print()

INDEED_URL = 'https://kr.indeed.com/jobs?q=%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C'
LIMIT = 50

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find('div',{'class' : 'pagination'})
    links = pagination.find_all('a')
    pages = []

    for  link in links[:-1]:
        pages.append(int(link.string))

    last_page = pages[-1]
    return last_page

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'scrapping {page+1}page')
        result = requests.get(f'{INDEED_URL}&start={page * LIMIT}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div',{'class' : 'jobsearch-SerpJobCard'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def extract_job(html):
    title = html.find('h2', {'class': 'title'}).find('a')['title']
    jobID = html.find('a')['id'].strip('jl_')
    company = html.find('span',{'class': 'company'})
    companyAnchor = company.find('a')
    location = html.find('span', {'class': 'location'}).string
    if companyAnchor != None:
        company = company.find('a').string
    else:
        company = company.string#.strip()
    return{'title':title, 'company':company, 'location':location, 'link':f'https://kr.indeed.com/viewjob?jk={jobID}'}


