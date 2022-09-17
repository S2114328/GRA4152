##
# this module defines the ComboLock class
##


class ComboLock : 
    ## intialize
    #
    def __init__(self):
        self._dial = 0
        self._n1 = 0 
        self._n2 = 0
        self._n3 = 0
    
    
    ## sets the lock to combination secret1, secret2, secret3
    #
    def ComboLock(self, secret1, secret2, secret3):
        self._secret1 = secret1
        self._secret2 = secret2
        self._secret3 = secret3
    
    ## reset dial
    #
    def reset(self):
           self._dial = 0
    ## saves number on dial
    #
    def save(self):
        if self._n1 == 0:
            self._n1 = self._dial
        elif self._n2 == 0:
            self._n2 = -self._dial
        elif self._n3 == 0:
            self._n3 = self._dial
        
    ## turn left
    #
    def turnLeft(self, ticks):
        self._dial = self._dial - ticks
            
    ## turn right
    #
    def turnRight(self, ticks):
         self._dial = self._dial + ticks
            
    ## open safe
    #
    def open(self):
        if (self._n1 == self._secret1) and (self._n2 == self._secret2) and (self._n3 == self._secret3):
            print("unlocked")
        else:
            print("incorrect combination")
    
    
