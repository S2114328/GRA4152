##
# this module defines the class BankAccount
#

## A bank account has a balance that can be changed by deposits and withdrawals.
#
class BankAccount :
    
    ## initialize
    #
    def __init__(self, initialBalance = 0.0) :
        self._balance = initialBalance
    
    ## deposit
    #
    def deposit(self, amount) :
        self._balance = self._balance + amount
        
    ## check balance
    #
    def getBalance(self) :
        return self._balance
    
    ## withdraw
    #
    def withdraw(self, amount) :
        PENALTY = 10.0
        if amount > self._balance :
            self._balance = self._balance - PENALTY
        else :
            self._balance = self._balance - amount
    ## interest
    #
    def addInterest(self, rate) :
        amount = self._balance * rate / 100.0
        self._balance = self._balance + amount
        
        
        