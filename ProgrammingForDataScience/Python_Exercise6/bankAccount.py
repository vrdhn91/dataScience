

class BankAccount:
    
    def __init__(self, pin, amount, oldpin, newpin):
        self.pin = pin
        self.amount = amount
        self.oldpin = oldpin
        self.newpin = newpin
    
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
        
print('Please create new account first!\n')
pin = input('Please setup your PIN: ')
amount = int(input('Please input your initial deposit: '))
ba = BankAccount(pin, amount, pin,'')
print('Your account is successfully created\n')

menu = 0
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
        curBal = ba.deposit(pin, amount)
    elif menu==2:
        pin = input('Please input your PIN: ')
        amount = int(input('Please input the amount: '))
        curBal = ba.withdraw(pin, amount)
    elif menu==3:
        pin = input('Please input your PIN: ')
        if ba.pin==pin:
            curBal = ba.get_balance(pin)
            print('Your current balance is: ', curBal,'\n')
        else: 
            print('Incorrect PIN. Please try again!\n')
    elif menu==4:
        pin = input('Please input your PIN: ')
        newpin = input('Please your New PIN: ')
        oldpin = pin
        curBal = ba.change_pin(oldpin, newpin)
        