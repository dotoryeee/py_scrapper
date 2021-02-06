import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36'
}


def makeURL(target_job):
    urls = ['https://stackoverflow.com/jobs?r=true&q=' + target_job,
            'https://weworkremotely.com/remote-jobs/search?term=' + target_job,
            'https://remoteok.io/remote-dev+' + target_job + '-jobs']
    return urls


def conn(url):
    print(f'connecting to {url}')
    r = requests.get(url, headers=headers)
    return r.text


# stackoverflow
def extractSO(data):
    print(f'Extracting SO')
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.find('div', class_='listResults')
    soup = soup.find_all('div', class_='fl1')
    datas = []
    for line in soup:
        try:
            title = line.find('h2').find('a')['title']
            company = line.find('h3').find('span').string.rstrip()
            link = line.find('h2').find('a')['href']
            datas.append([title, company, 'https://stackoverflow.com' + link])
        except:
            pass
    return datas


# weworkremotely
def extractWWR(data):
    print(f'Extracting WWR')
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.find_all('li', class_='feature')
    datas = []
    try:
        for line in soup:
            title = line.find('span', class_='title').string
            company = line.find('span', class_='company').string
            link = line.find('a')['href']
            datas.append([title, company, 'https://weworkremotely.com' + link])
    except:
        pass
    return datas


# remoteok
def extractRO(data):
    print(f'Extracting RO')
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.find('table', id='jobsboard')
    soup = soup.find_all('td', class_='company_and_position')
    datas = []
    for line in soup:
        try:
            title = line.find('a', class_='preventLink').find('h2').string
            link = line.find('a', class_='preventLink')['href']
            company = line.find('a', class_='companyLink').find('h3').string
            datas.append([title, company, 'https://remoteok.io/' + link])
        except:
            pass
    return datas


# test
# print(extractSO(conn('https://stackoverflow.com/jobs?r=true&q=python')))
# print(extractWWR(conn('https://weworkremotely.com/remote-jobs/search?term=python')))
#print(extractRO(conn('https://remoteok.io/remote-dev+python-jobs')))
