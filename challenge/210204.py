import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import json

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36'}

"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


def conn(url):
    print(f'connecting to {url}')
    r = requests.get(url, headers=headers)
    return (r.text)


def extractDict(data):
    print('extracting html')
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.find('body')
    soup = soup.find('script', id='data').string
    return soup[14:len(soup) - 1]  # 앞 뒤로 글자 자르기


def dataToDict(data):
    print('extracting dict')
    data = json.loads(data)
    return data


def getParameter():
    try:
        parameter = request.args
        return parameter
    except:
        return None


def makeUrl(param):
    url = 'https://www.reddit.com/r/javascript'  # +param
    return url


# DAO
# conn -> extractDict -> extractData
def MakeInfo(url):
    data = conn(url)
    data = extractDict(data)
    data = dataToDict(data)
    data = data['posts']['models']
    datas = []
    print('building Information')
    for line in data.values():
        title = line['title']
        score = line['score']
        url = line['permalink']
        data = [title, score, url]
        datas.append(data)
    print('start rendering')
    return datas


app = Flask("DayEleven")


@app.route('/')
def home():
    return render_template('home.html', list=subreddits)


@app.route('/read')
def board():
    param = getParameter()
    print(f'parameter : {param}')
    url = makeUrl(param.keys())
    print(f'access board page({param.keys()})')
    data = MakeInfo(url)
    return render_template('read.html', data=data)


app.run(host='localhost')
