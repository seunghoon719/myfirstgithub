import requests
from bs4 import BeautifulSoup

def hh():
    requests
    requests.get("https://finance.naver.com/item/main.nhn?code=005380")
    r = requests.get("https://finance.naver.com/item/main.nhn?code=005380")
    soup = BeautifulSoup(r.text,'html.parser')
    print("현대차 시가는"+soup.select_one(".no_today .blind").text+"원 입니다.")

def nn():
    requests
    requests.get("https://finance.naver.com/item/main.nhn?code=035420")
    r = requests.get("https://finance.naver.com/item/main.nhn?code=035420")
    soup = BeautifulSoup(r.text, 'html.parser')
    print("네이버 시가는"+soup.select_one(".no_today .blind").text +"원 입니다.")

hh()
nn()

def aa(x,y):
    print("상엽님은 현대차 {0}주, 네이버 {1}주를 보유하고 계십니다.".format(x,y))
    requests.get("https://finance.naver.com/item/main.nhn?code=005380")
    r = requests.get("https://finance.naver.com/item/main.nhn?code=005380")
    soup = BeautifulSoup(r.text,'html.parser')
    h = soup.select_one(".no_today .blind").text.replace(',','')
    h = int(h)
    h1 = h*int(x)

    print("현대차는"+"{0:,}".format(h1)+ "원")

    requests.get("https://finance.naver.com/item/main.nhn?code=035420")
    r = requests.get("https://finance.naver.com/item/main.nhn?code=035420")
    soup = BeautifulSoup(r.text, 'html.parser')
    n = soup.select_one(".no_today .blind").text.replace(',','')
    n = int(h)
    n1 = h*int(y)

    print("네이버는"+"{0:,}".format(n1)+"원")

    sum = int(h1)+int(n1)

    print("상엽님의 주식자산은 총"+"{0:,}".format(sum)+"원 입니다.")

aa(5,41)
