class Hotel:
    ac_room_available = [False,False,False,False,False]
    non_ac_room_available = [False,True,True,True,False]
    
    # Here we create a method that checks the Ac rooms is available or not
    def ac_room_availability_checker(self):
        # This loop is check the room is available or not if Ac rooms is available !
        # The next process is continue
        for i in range(len(self.ac_room_available)):
            if(self.ac_room_available[i] == True):
                self.ac_room_available[i] = False
                return True
        return False
    
    def non_ac_room_availability_checker(self):
        #This loop the Availability of the non Ac rooms
        for i in range(len(self.non_ac_room_available)):
            if(self.non_ac_room_available[i] == True):
                self.non_ac_room_available[i] = False
                return True
        return False

    def available_rooms(self):
        count = 0
        length = len(self.ac_room_available) + len(self.non_ac_room_available)
        for i in range(length):
            if(True == i):
                count += 1
            
        return count
    
    # Check the Dates is  valid or not
    def is_date_valid(self,day,month,year):
        # 90 percent are clear here
        if (year <= 9999 and year >= 1000) and (month <= 12 and month >= 1) and (day <= 31 and day >= 1) :
        
            if (((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)) and month == 2 ) and day <= 29:
                return True

            
            if day == 31 and month not in (1,3,5,7,8,10,12):
                return False

            if month == 2 and day > 28:
                return False
            
            return True

        else:
            return False
        



