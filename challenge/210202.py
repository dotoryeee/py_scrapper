import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# URL접속후 JSON 리터해주기
def conn(url):
    r = requests.get(url)
    return r.json()


def make_detail_url(id):
    return f"{base_url}/items/{id}"


def getNewsData(target):
    print(f'connect to NEWS : {target}')
    try:  # db{}에 이미 데이터가 있으면 그거 찾아서 반환
        already = db[target]
        print('data loaded from DB')
        return already
    except:
        data = conn(target)
        db[target] = data
        print('new data downloaded')
        return data

def getBoardData(target):
    print(f'connect to BOARD : {target}')
    data = conn(target)
    print(data)


def extractNewsList(data):
    reprocessData = []
    try:
        for list in data["hits"]:
            title = list['title']
            url = list['url']
            points = list['points']
            author = list['author']
            num_comments = list['num_comments']
            reprocessData.append([title, url, points, author, num_comments])
    except:
        pass
    return reprocessData


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api


db = {}  # CACHE DB
app = Flask("My HK News")


@app.route('/')
def home():
    data = getNewsData(popular)
    data = extractNewsList(data)
    return render_template('HKnews.html', data=data)


@app.route('/<id>')
def targetID(id):
    boardURL = make_detail_url(id)
    data = getBoardData(boardURL)
    return id


@app.route('/?order_by=<option>')
def sortedlist(option):
    if option == 'new':
        data = getNewsData(new)
        data = extractNewsList(data)
        return 'order by new'
    else:
        data = getNewsData(popular)
        data = extractNewsList(data)
        return 'order by popular'


app.run(host="localhost")