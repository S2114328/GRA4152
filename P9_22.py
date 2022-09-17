##
# this module defines the Portfolio class
# NOTE: please have the file W9_1 in your folder use the BankAccount class
##

from W9_1 import BankAccount

class Portfolio :
    def __init__(self, checking = 0, savings = 0):
        self._checking = BankAccount(checking)
        self._savings= BankAccount(savings)
    
    def deposit(self, amount, account):
        if account == "S":
            self._savings.deposit(amount)
        elif account == "C":
            self._checking.deposit(amount)
        
    def withdraw(self, amount, account):
        if account == "S":
            self._savings.withdraw(amount)
        elif account == "C":
            self._checking.withdraw(amount)
    
    def transfer(self, amount, account):
        if account == "S":
            o = self._savings.getBalance()
            self._savings.withdraw(amount)
            if amount > o:
                print("insufficient funds, penalty applied")
            else:
                self._checking.deposit(amount)
            
        elif account == "C":
            o = self._checking.getBalance()
            self._checking.withdraw(amount)
            if amount > o:
                print("insufficient funds, penalty applied")
            else:
                self._savings.deposit(amount)
    
    def getBalance(self, account):
        if account == "S":
            return self._savings.getBalance()
        elif account == "C":
            return self._checking.getBalance()