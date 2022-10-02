class Bank_Account:
    balance = 10000

    def __init__(self, a):
        self.balance = self.balance+a

    def __init__(self, a, b):
        if b == 1:
            self.balance = a
        else:
            self.balance = self.balance+a

    def setInterest(self):
        self.balance = self.balance+(self.balance*10*2)/100

    def getAmount(self):
        return self.balance


a = Bank_Account(int(input("Enter your amount : ")), 1)
a.setInterest()
amount = a.getAmount()
print("He got: ", amount)
