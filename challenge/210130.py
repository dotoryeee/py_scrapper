import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

URL_iban = "https://www.iban.com/currency-codes"
URL_twise = "https://transferwise.com/gb/currency-converter/"
currency_code_data = []

def conn(url):
    r = requests.get(url)
    return r.text

def catchList(data):
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find('table', class_='table')
    li = table.find_all('td')
    for i in li:
        currency_code_data.append(i.string)
    printList()

def catchCurrency(data):
    soup = BeautifulSoup(data, 'html.parser')
    converted = soup.find('span', class_='text-success')
    return converted.string

def printList():
    country = []
    for i, data in enumerate(currency_code_data):
        i += 1
        country.append(data)
        if i % 4 == 0:
            print(f'# {int(i/4)} {country[0]}')
            country.clear()

def selectNum():
    while True:
        num = input('#: ')
        try:
            num = int(num)
            return num
        except:
            print('that wasnt a number')

def findCurrency(num):
    if num >= 2:
        num *= 4
        num -= 3
    catch = currency_code_data[num-1:num+3]
    print(f'you selected {catch[0]}')
    print(f'{catch[0]} s currency is {catch[1]}({catch[2]})')
    return catch[2]

def main():
    global URL_twise
    while True:
        #Iban에서 통화코드 가져오기
        data1 = conn(URL_iban)
        print('welcome to currencyconvert pro 2000\n')
        catchList(data1)

        #환전을 위해 사용자 입력받기 시작
        print('where are you from? choose a country by number\n')
        origin = selectNum()  #오리지널 국가 숫자 확인
        origin = findCurrency(origin) #오리지널 통화코드로 변경

        print('now choose another country\n')
        target = selectNum() #통화변경 타겟국가 숫자 확인
        target = findCurrency(target) #타겟국가 통화코드로 변경

        #환전량 입력
        print(f'how many {origin} -> {target}?')
        while True:
            try:
                amount = input()
                break
            except:
                print('that wasnt a number. type again')

        #환율 가져오기 시작
        URL_twise = URL_twise+origin+'-to-'+target+'-rate?amount='+amount
        #print(URL_twise)
        data2 = conn(URL_twise)
        converted = catchCurrency(data2)
        print(f'{amount}{origin} = {converted+amount}{target}')

        while True:
            yn = input('do you want to try again? y/n : ')
            if yn == 'N' or 'n':
                break

        format_currency(converted, "KRW", locale="ko_KR")
main()




