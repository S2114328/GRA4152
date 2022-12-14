##
# This module defines the Person Superclass and the Student and Instructor subclasses
#

class Person:
    ## initialize variables
    # @ name : name of person
    # @ YoB: year of birth of person
    def __init__(self, name = "not provided", YoB = "not provided"):
        self._name = name
        self._YoB = YoB
    ## print person object
    #       
    def __repr__(self):
        return self._name + " , " + str(self._YoB)

#define the subclass

class Student(Person):
    ##initialize variables
    # @ name: name of person
    # @ YoB: year of birth of person
    # @ major: major of study
    
    def __init__(self, name = "not provided", YoB = "not provided", major = "not provided"):
        super().__init__(name,YoB)
        self._major = major
    ## print student object
    #
    def __repr__(self):
        return self._name + " , " + str(self._YoB) + " , " + self._major
        
class Instructor(Person):
    ##initialize variables
    # @ name: name of person
    # @ YoB: year of birth of person
    # @ salary: salary of instructor
    def __init__(self, name = "not provided", YoB = "not provided", salary = "not provided"):
        super().__init__(name, YoB)
        self._salary = salary
    ## print
    #
    def __repr__(self):
        return self._name + " , " + str(self._YoB) + " , " + self._salary        

print( "### Tester Program ###")
n = input("Name: ")
y = input("Year of Birth: ")
p = Person(n,y )
print("Output :", p)
print("Expected :", n, " , ",  y)
m = input("major :")
s = Student(n,y,m)
print("Output :", s)
print("Expected :", n, " , ",  y, " , ", m)
sa = input("salary :")
i = Instructor(n,y,sa)
print("Output :", i)
print("Expected :", n, " , ",  y, " , ", sa)
