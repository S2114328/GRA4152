##
# This module defines the customer class
#

class Customer:
    ## initialize
    #
    def __init__(self):
        self._total = 0
    
    ## make purchase
    #
    def makePurchase(self, amount):
        self._total = self._total + amount
        
    ## cumulative discounts earned
    # 
    def discountReached(self):
        return (self._total // 100) *10
