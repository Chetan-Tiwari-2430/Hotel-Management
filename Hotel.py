class Hotel:
    ac_room_available = [False,False,False,True,True]
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
    

