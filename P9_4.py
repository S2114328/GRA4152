##
#  This module defines the Address class.
#

class Address :
    ## intialize
    #
    def __init__(self, street, city, state, pcode,apnum = None):
        self._apnum = apnum
        self._street = street
        self._city = city
        self._state = state
        self._pcode = pcode
    
    ## print address
    #
    def Print(self):
        print(self._street)
        print(self._city, self._state, self._pcode)
    
    ## returns post code of addy
    #
    def pcode(self):
        return self._pcode
    
    ## test whether come before or after other Address based on postal code
    #
    def comesBefore(self, other):
        if int(self._pcode) > int(other.pcode()):
            print("After")
        else:
            print("Before")