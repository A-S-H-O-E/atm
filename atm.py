class ATM:
    def __init__(self,balance,pin,name):
        self.balance=balance
        self.pin = pin
        self.name = name
    
    def checkbalance(self):
        p=int(input('Enter your pin : '))
        if(p==self.pin):
            print('The balance in the account is ' + str(self.balance)) 
        else:
            print('Incorrect pin')
    def deposit(self):
        p=int(input('Enter Pin : '))
        if(p==self.pin):
            a=int(input('Deposit money : '))
            self.balance = self.balance+a
            print('The new balalnce is : ' + str(self.balance))
        else:
            print('Incorrect pin')
    def withdraw(self):
        p=int(input('Enter Pin : '))
        if(p==self.pin):
            a=int(input('How much money to you want to withdraw '))
            if(a>self.balance):
                print('You dont have enogh money')
            else:
                self.balance = self.balance - a
                print('The new balalnce is : ' + str(self.balance))
        else:
            print('Incorrect Pin')

Customer1=ATM(5000,1234,'Aashrith')
Customer1.checkbalance()
Customer1.deposit()
Customer1.withdraw()

    