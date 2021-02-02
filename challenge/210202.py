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
    return data


def extractNewsList(data):
    reprocessData = []
    try:
        for list in data["hits"]:
            title = list['title']
            url = list['url']
            points = list['points']
            author = list['author']
            num_comments = list['num_comments']
            objectID = list['objectID']
            reprocessData.append([title, url, points, author, num_comments, objectID])
    except:
        pass
    return reprocessData


def extractBoardList(data):
    dataDict = {}
    dataDict["title"] = data["title"]
    dataDict["points"] = data["points"]
    dataDict["author"] = data["author"]
    dataDict["url"] = data["url"]
    comments = []
    for i in data["children"]:
        if i['author'] == 'null':
            break
        comment = []
        comment['author'] = i['author']
        comment['text'] = i['text']
        comments.append(comment)
    dataDict['comments'] = comments
    return dataDict


def getParameter():
    try:
        parameter = request.args.get('order_by')
        return parameter
    except:
        return None


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api


db = {}  # CACHE DB
app = Flask("My HK News")


@app.route('/')
def home():
    parameter = getParameter()
    print(f'{parameter} parameter received')
    if parameter == 'new':
        print('new page call')
        data = getNewsData(new)
    elif parameter is None or "popular":
        print('popular page call')
        data = getNewsData(popular)
    else:
        return 'param error'
    data = extractNewsList(data)
    return render_template('HKnews.html', data=data)


@app.route('/<id>')
def targetID(id):
    boardURL = make_detail_url(id)
    data = getBoardData(boardURL)
    #data = extractBoardList(data)
    return render_template('board.html', data=data)


app.run(host="localhost")
