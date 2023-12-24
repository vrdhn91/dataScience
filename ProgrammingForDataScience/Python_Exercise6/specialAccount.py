

class SavingsAccount:
    
    def __init__(self, pin, amount, oldpin, newpin):
        self.pin = pin
        self.amount = amount
        self.oldpin = oldpin
        self.newpin = newpin
        self.interestRate = 0.1
    
    def deposit(self, pin, amount):
        if self.pin == pin:
            self.amount+=amount
            print('Deposit is success!\nYour current balance is: ', self.amount,'\n')
        else: 
            print('Incorrect PIN. Please try again!')
        return self.amount
    
    def withdraw(self, pin, amount):
        if self.pin == pin:
            self.amount-=amount
            print('Withdrawal is success!\nYour current balance is: ', self.amount,'\n')
        else: 
            print('Incorrect PIN. Please try again!')
        return self.amount
    
    def get_balance(self, pin):
        return self.amount
    
    def change_pin(self,oldpin, newpin):
        if self.pin != oldpin:
            print('Incorrect PIN. Please try again!')
        else:
            self.pin = newpin
            print('PIN is changed succesfully')
    
    def balanceWithInterest(self,pin):
        self.amount = self.amount + (self.amount*self.interestRate)
        print('The interest rate is: ', self.interestRate)
        return self.amount
            
class FeeSavingsAccount:
    
    def __init__(self, pin, amount, oldpin, newpin):
        self.pin = pin
        self.amount = amount
        self.oldpin = oldpin
        self.newpin = newpin
        self.withdrawalFee = 10
    
    def deposit(self, pin, amount):
        if self.pin == pin:
            self.amount+=amount
            print('Deposit is success!\nYour current balance is: ', self.amount,'\n')
        else: 
            print('Incorrect PIN. Please try again!')
        return self.amount
    
    def withdraw(self, pin, amount):
        if self.pin == pin:
            self.amount = self.amount - self.withdrawalFee-amount
            print('Withdrwal fee: ', self.withdrawalFee)
            print('Withdrawal is success!\nYour current balance is: ', self.amount,'\n')
        else: 
            print('Incorrect PIN. Please try again!')
        return self.amount
    
    def get_balance(self, pin):
        return self.amount
    
    def change_pin(self,oldpin, newpin):
        if self.pin != oldpin:
            print('Incorrect PIN. Please try again!')
        else:
            self.pin = newpin
            print('PIN is changed succesfully')

print('Please choose your account type:\n(1) Savings Account\n(2) Fee Savings Account:\n')
accountType = int(input('Input: '))
        
print('\nPlease create new account first!\n')
pin = input('Please setup your PIN: ')
amount = int(input('Please input your initial deposit: '))
sa = SavingsAccount(pin, amount, pin,'')
fsa = FeeSavingsAccount(pin, amount, pin,'')
print('Your account is successfully created\n')

menu = 0
if accountType == 2:
    while menu!=5:
        print('''Please insert a number for your transaction:
            1. Deposit
            2. Withdraw
            3. Get Balance
            4. Change PIN
            5. Exit''')
        menu = int(input('Your Input: '))
        if menu==1:
            pin = input('Please input your PIN: ')
            amount = int(input('Please input the amount: '))
            curBal = fsa.deposit(pin, amount)
        elif menu==2:
            pin = input('Please input your PIN: ')
            amount = int(input('Please input the amount: '))
            curBal = fsa.withdraw(pin, amount)
        elif menu==3:
            pin = input('Please input your PIN: ')
            if fsa.pin==pin:
                curBal = fsa.get_balance(pin)
                print('Your current balance is: ', curBal,'\n')
            else: 
                print('Incorrect PIN. Please try again!\n')
        elif menu==4:
            pin = input('Please input your PIN: ')
            newpin = input('Please your New PIN: ')
            oldpin = pin
            curBal = fsa.change_pin(oldpin, newpin)
            
elif accountType == 1:
    while menu!=6:
        print('''Please insert a number for your transaction:
            1. Deposit
            2. Withdraw
            3. Get Balance
            4. Change PIN
            5. Check Balance with Interest
            6. Exit''')
        menu = int(input('Your Input: '))
        if menu==1:
            pin = input('Please input your PIN: ')
            amount = int(input('Please input the amount: '))
            curBal = sa.deposit(pin, amount)
        elif menu==2:
            pin = input('Please input your PIN: ')
            amount = int(input('Please input the amount: '))
            curBal = sa.withdraw(pin, amount)
        elif menu==3:
            pin = input('Please input your PIN: ')
            if sa.pin==pin:
                curBal = sa.get_balance(pin)
                print('Your current balance is: ', curBal,'\n')
            else: 
                print('Incorrect PIN. Please try again!\n')
        elif menu==4:
            pin = input('Please input your PIN: ')
            newpin = input('Please your New PIN: ')
            oldpin = pin
            curBal = sa.change_pin(oldpin, newpin)
        elif menu == 5:
            pin = input('Please input your PIN: ')
            if sa.pin==pin:
                curBal = sa.balanceWithInterest(pin)
                print('Your balance with interest is: ', curBal,'\n')
            else: 
                print('Incorrect PIN. Please try again!\n')