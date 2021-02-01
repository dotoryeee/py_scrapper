import requests
from bs4 import BeautifulSoup

URL = "https://www.iban.com/currency-codes"
currency_data = []


def conn(url):
    r = requests.get(url)
    return r.text


def catchList(data):
    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find('table', class_='table')
    list = table.find_all('td')
    for i in list:
        currency_data.append(i.string)
    printList()


def printList():
    country = []
    for i, data in enumerate(currency_data):
        i += 1
        country.append(data)
        if i % 4 == 0:
            print(f'# {int(i / 4)} {country[0]}')
            country.clear()


def selectNum():
    print('choose a number from the list')
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
    catch = currency_data[num - 1:num + 3]
    print(f'you selected {catch[1]}')
    print(f'{catch[0]} s currency is {catch[1]}({catch[2]})')


def main():
    while True:
        data = conn(URL)
        catchList(data)
        selected = selectNum()
        findCurrency(selected)
        yn = input('do you want to try again? y/n : ')
        if yn == 'N' or 'n':
            break


main()
