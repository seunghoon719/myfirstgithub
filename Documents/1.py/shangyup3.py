from bs4 import BeautifulSoup
import requests
import datetime

# stock_id = input('What is the stock id?: ')
url = "https://finance.naver.com/item/main.nhn?code="

def qq(name, stock_id, num):
    r = requests.get(url + stock_id)
    soup = BeautifulSoup(r.text,'html.parser')
    result = name+ "시가는"+soup.select_one(".no_today .blind").text + "원 이고"
    print(result)
    print(str(num)+"개 보유하고 계십니다.")
    money = soup.select_one(".no_today .blind").text.replace(",","")
    money = int(money)
    b = int(money * num)
    print(name+"주식 자산은 총"+"{0:,}".format(b)+"원 입니다.")
    return b


q1 = qq("현대차", "005380", 5)
q2 = qq("네이버", "035420", 41)

def sum(x,y):
    return x+y

w = sum(q1, q2)

f = open('1.txt', 'wb')

f.write(bytes(w))
f.close()

print("상엽님의 총 주식자산은 {0:,}원 입니다.".format(w))
