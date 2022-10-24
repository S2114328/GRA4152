
##
# This module defines the Appointment superclass that can save to a file
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
        self.save_date = date
    # checks whether occurs on this date
    def occursOn(self, year, month, day):
        if (day == self.getDate()[0])&(month ==self.getDate()[1])&(year == self.getDate()[2]):
            return True
        else:
            return False
        
    # save the appointment to a text file
    def save(self, filename = "appointments.txt"):
        file = open(filename, "a")
        info  = "onetime" + "," + self.getDesc()+ ","+ self.save_date + "\n"
        file.write(info)
        file.close()
        
        
class Daily(Appointment):
    # constructs a daily appointment
    # @param desc, appointment description
    def __init__(self, desc):
        super().__init__(desc, "000000")
        self.save_date = "000000"
    # checks whether occurs on this date
    def occursOn(self, year, month, day):
        return True
    
    # save the appointment to a text file
    def save(self, filename = "appointments.txt"):
        file = open(filename, "a")
        info  = "daily" + "," + self.getDesc()+ ","+ self.save_date + "\n"
        file.write(info)
        file.close()
    
class Monthly(Appointment):
    # constructs a monthly appointment
    # @param desc, appointment description
    # @param day, the day of the appointment
    def __init__(self, desc, day):
        if len(str(day)) == 1: day = "0"+str(day)
        super().__init__(desc, str(day)+"0000")
        self.save_date = str(day)+"0000"
    
    # checks whether occurs on this date
    def occursOn(self, year, month, day):
        if day == self.getDate()[0]:
            return True
        else:
            return False
    
    # save the appointment to a text file
    def save(self, filename = "appointments.txt"):
        file = open(filename, "a")
        info  = "monthly" + "," + self.getDesc()+ ","+ self.save_date + "\n"
        file.write(info)
        file.close()



## loader function
def load(filename = "appointments.txt"):
    # Opens text file from working directory
    file = open(filename, "r")

    # emtpy list
    appointments = []
    
    # Loop to obtain appointments
    for i in file:
        components = i.rstrip("\n").split(",")
        
        if components[0] == "onetime":
            appointments.append(Onetime(components[1], components[2]))
        elif components[0] == "monthly":
            appointments.append(Monthly(components[1], int(components[2][0:2])))
        elif components[0] == "daily":
            appointments.append(Daily(components[1]))
    
    # close file
    file.close()
    
    # Returns appointments
    return appointments



















