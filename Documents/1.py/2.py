def deposit(balance, money):  #입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(blalance, money):  #출금
    if balance >= money: #
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return blalance

def witdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료
    return commission, balance - money - commission



balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)
