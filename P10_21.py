##
# This module defines the BankAccount superclass and its hierarchy
##

class BankAccount :
    ## Constructs a bank account
    #
    penalty = 10.0
    def __init__(self) :
        self._balance = 0.0
    ## add funds
    #
    def deposit(self, amount) :
        self._balance = self._balance + amount
        print("new balance :", self._balance)
    ## withdraw funds, penalty if withdraw more than available
    #
    def withdraw(self, amount) :
        if self.getBalance()<amount:
            print("insufficient balance")
            self._balance = self._balance - BankAccount.penalty
            print("new balance: ", self.getBalance())
        else:
            self._balance = self._balance - amount
            print("new balance :", self.getBalance())
    ## returns the balance
    #
    def getBalance(self) :
        return self._balance
    ## to be defined in subclass
    #
    def monthEnd(self) :
        return 

## A savings account earns interest on the minimum balance.
#
class SavingsAccount(BankAccount) :
    ## Constructs a savings account with a zero balance.
    #
    def __init__(self) :
        super().__init__()
        self._rate = 0
        self._minbal = super().getBalance()
    ## Sets the interest rate for this account.
    # @param rate the monthly interest rate in percent
    #
    def setInterestRate(self, rate) :
        self._rate = rate
    ## withdraw funds
    #
    def withdraw(self, amount) :
        super().withdraw(amount)
        if self.getBalance() < self._minbal:
            self._minbal = self.getBalance()
    ## add interest to account
    #
    def monthEnd(self) :
        interest = self._minbal*self._rate/100
        self.deposit(interest)
        self._minbal = self.getBalance()

## A checking account has a limited number (3) of free deposits and withdrawals.
#
class CheckingAccount(BankAccount) :
    ## Constructs a checking account with a zero balance.
    #
    def __init__(self) :
        super().__init__()
        self._count = 0
    ## calculate whether next transaction incurs a fee
    #
    def feeComp(self):
        self._count += 1
        if self._count >3:
            return 1
        else:
            return 0
    ## deposit
    #
    def deposit(self, amount):
        super().deposit(amount-self.feeComp())
    ## withdraw
    #
    def withdraw(self, amount) :
        super().withdraw(amount+self.feeComp())
    ## reset transaction counter
    def monthEnd(self) :
        print("closing balance: ", self.getBalance())
        self._count = 0