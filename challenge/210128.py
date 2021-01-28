import requests
import sys

def checkHTTP(url):
    if url[:4] != 'http':
        url = 'http://' + url
    return url

def checkDOT(url):
    if '.' not in url:
        return False
    else:
        return True

def checkStatus(url):
    r = requests.get(url)
    return r.status_code

def main():
    print('welcome to IsItDown? py!\nplease write URL or URLs you want to check(seperate by comma)')
    urls = sys.stdin.readline().split()
    for url in urls:
        #http 확인 후 없으면 붙이기
        url = checkHTTP(url)
        #URL에 '.'이 있는 주소인지 확인
        dotCheck = checkDOT(url)
        if dotCheck == False:
            print(f'{url} is bad URL')
            break
        else:
            code = checkStatus(url)
        if code == 200:
            print(f'{url} is up')
        else:
            print(f'{url} is down')
while True:
    main()
    ask = input('do you want to start over? y/n : ')
    if ask == 'n' or 'N':
        break