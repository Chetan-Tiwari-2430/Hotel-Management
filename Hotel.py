class Hotel:
    is_room_available = [False,False,False,True,True]
    
    # Here we create a method that checks the room is available or not
    def room_availability_checker(self):
        for i in range(len(self.is_room_available)):
            if(self.is_room_available[i] == True):
                self.is_room_available[i] = False
                return True
        return False
    

