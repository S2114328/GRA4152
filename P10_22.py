##
# This module defines the Appointment superclass
##


class Appointment:
    # Constructs an Appointment with description and date
    # @param desc is the description of the appoinment
    # @param date is the date of the appointment
    def __init__(self, desc, date):
        self._desc = desc
        if len(date) != 6:
            print("Date must be mmddYY!")
            raise ValueError
        else:
            self._date = [int(date[0:2]), int(date[2:4]), int(date[4:])]
    
    # to be defined
    def occursOn(self):
        raise NotImplementedError()
    
    # returns date of appointment
    def getDate(self):
        return self._date
    
    # returns description of appointment
    def getDesc(self):
        return self._desc
    
class Onetime(Appointment):
    # constructs a onetime appointment
    # @param desc, appointment description
    # @param date, the date of the appointment
    def __init__(self, desc, date):
        super().__init__(desc, date)
    
    # checks whether occurs on this date
    def occursOn(self, year, month, day):
        if (day == self.getDate()[0])&(month ==self.getDate()[1])&(year == self.getDate()[2]):
            return True
        else:
            return False
        
class Daily(Appointment):
    # constructs a daily appointment
    # @param desc, appointment description
    def __init__(self, desc):
        super().__init__(desc, "000000")
    # checks whether occurs on this date
    def occursOn(self, year, month, day):
        return True
    
class Monthly(Appointment):
    # constructs a monthly appointment
    # @param desc, appointment description
    # @param day, the day of the appointment
    def __init__(self, desc, day):
        if len(str(day)) == 1: day = "0"+str(day)
        super().__init__(desc, str(day)+"0000")
    
    # checks whether occurs on this date
    def occursOn(self, year, month, day):
        if day == self.getDate()[0]:
            return True
        else:
            return False

## Tester code
Appointments = [Daily("brushteeth"), Monthly("Gym", 7), Monthly("Gym", 11), Onetime("dentist", "111022")]

# Date to check 

date = input("Please input a day (ddmmYY) : ")

# check
for i in Appointments:
    if i.occursOn(int(date[4:]), int(date[2:4]), int(date[:2])) == True:
        print("we found a match! : ", i.getDesc())









