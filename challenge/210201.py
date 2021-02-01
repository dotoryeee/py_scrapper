import csv
import requests
from bs4 import BeautifulSoup

alba_url = "http://www.alba.co.kr"


def conn(url):  # 페이지 연결
    r = requests.get(url)
    return r.text


def getLinks(data):  # 알바천국 메인 페이지에서 브랜드별 링크주소 긁어오기
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.find('div', id='MainSuperBrand').find('ul', class_='goodsBox')
    soup_for_title = soup.find_all('strong')
    titles = []
    for title in soup_for_title:
        titles.append(title.string)
    soup_for_links = soup.find_all('a', class_='goodsBox-info')
    links = []
    for line in soup_for_links:
        links.append(line.get('href'))
    return titles, links


def getJobs(url):  # 브랜드별 공고 긁어오기
    data = conn(url)
    soup = BeautifulSoup(data, 'html.parser')
    soup = soup.find('div', class_='goodsList').find('tbody')
    soup = soup.find_all('tr', class_='')
    alba_datas = []
    for line in soup:
        # 위치정보
        try:
            location = line.find('td', class_='local first').get_text()
        except:
            location = '위치정보없음'
        # 공고제목
        try:
            title = line.find('span', class_='title').string
        except:
            title = "공고제목없음"
        # 시간정보
        try:
            time = line.find('span', class_='time').string
            if time == None:
                time = line.find('span', class_='consult').string
        except:
            time = '시간정보없음'
        # 시급정보
        try:
            pay = line.find('td', class_='pay').find('span', class_='number').string
        except:
            pay = "시급정보없음"

        data = {}
        data['location'] = location
        data['title'] = title
        data['time'] = time
        data['pay'] = pay
        alba_datas.append(data)
    return alba_datas


def exportCSV(title, alba_datas):  # CSV출력
    field_names = ['location', 'title', 'time', 'pay']
    # newline = ''을 입력하면 csv 라인공백을 제거할 수 있다
    try:
        with open(title + '.csv', 'w+', newline='', encoding='utf') as f:
            print(f'exporting {title}.csv', end='')
            write = csv.writer(f)
            write.writerow(field_names)
            for data in alba_datas:
                print('.', end='')
                write.writerow([data['location'], data['title'], data['time'], data['pay']])
            print('complete!')
    except:
        pass


def main():
    data = conn(alba_url)
    titles, links = getLinks(data)
    for num, link in enumerate(links):
        alba_datas = getJobs(link)
        exportCSV(titles[num], alba_datas)


main()
