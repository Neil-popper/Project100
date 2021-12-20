money=1000
cash=0

class Atm(object):
    def __init__(self,CardNumber,PinNumber):
        self.PinNumber=PinNumber
        self.CardNumber=CardNumber
    def BalanceRemaining(self):
        money=1000
        if(cash<=money):
            money=money-cash
        print("accelerated")

def CashWithdrawl():
        cash=int(input("How much Money to you want to take out?"))
        money=1000
        if(cash<=money):
            money=money-cash
            print("Your remaining balance is $"+str(money))
        else:
            print("You don't have enough money in your acount")

def BalanceInquiry():
        print("You have $"+str(money))

Atm1=Atm("1000589362","185076")

test=input("Do you want to know your Card number, Pin number, Balance, or take out Cash ")
if(test=="Card number"):
    print(Atm1.CardNumber)
elif(test=="Pin number"):
    print(Atm1.PinNumber)
elif(test=="take out Cash"):
    CashWithdrawl()
elif(test=="Balance"):
    BalanceInquiry()