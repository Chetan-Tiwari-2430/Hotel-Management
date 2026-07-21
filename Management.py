from Hotel import Hotel
class Management:
    ac_rooms_price = 1000
    non_ac_rooms_price = 800
    cost = 0
    days = 0
    name = None
    age = None


    def user_interface(self):
        print("The Grand XYZ Hotel")
        print("1. Book Room")
        print("2. Show the Price")
        print("0. Exit")
        while True:
            try:
                choice = int(input("Enter Your Choice: "))
                break
            except:
                print("Enter Only the Number")
        match choice:
            case 1:
                self.book_room()
            case 2:
                self.show_room_prices()
            case 0:
                print("Thankyou For the Use")
                return
            case _:
                print("Enter only 0 to 2")
    
    


    def book_room(self):

        print("1. For Ac rooms")
        print("2. For Non-Ac rooms")
        while True:
            try:
                choice = int(input("Enter Your choice: "))
                if choice in (1,2):
                    break
                else:
                    print("Enter Only 1 and 2")
            except:
                print("Enter only Number's ")

        if (choice in (1,2)):
            self.allocation(choice)
    
    def show_price(self):
        print(f"Ac Rooms Price {self.ac_rooms_price}")
        print(f"Non Ac Rooms Price {self.non_ac_rooms_price}")
        
    
    def allocation(self,choice):
        if choice == 1:
            self.ac_room_booking()
        else:
            self.non_ac_room_booking()

    def check_room(self,number):
        self.hotel = Hotel()
        if number == 1:
            result_1 = self.hotel.ac_room_availability_checker()
            return result_1
        else:
            result_2 = self.hotel.non_ac_room_availability_checker()
            return result_2


    def ac_room_booking(self):
        flag = self.check_room(1)
        if flag:
            while True:
                try:
                    self.name = input("Enter Your Name: ")
                    self.age = int(input("Enter Your Age: "))
                    self.days = int(input("How Many days you have to stay: "))
                    print("Room Booked Successful")
                    self.cost =  int(self.days*self.ac_rooms_price)
                    self.bill()
                    break
                except:
                    print("Enter The Number of the age and days")
        else:
            print("Sorry to say ")
            print("But")
            print("Ac Rooms is not Available")

    def non_ac_room_booking(self):
        flag = self.check_room(2)
        print(flag)
        if flag:
            while True:
                try:
                    self.name = input("Enter Your Name: ")
                    self.age = int(input("Enter Your Age: "))
                    self.days = int(input("How Many days you have to stay: "))
                    print("Room Booked Successful")
                    self.cost =  int(self.days*self.ac_rooms_price)
                    self.bill()
                    break
                except:
                    print("Enter The Number of the age and days")
                    print("Plz Re-enter These information")
        else:
            print("Sorry to say ")
            print("But")
            print("Ac Rooms is not Available")

    def bill(self):
        one_day_cost = self.cost/self.days
        tax = (self.cost // 100) * 18
        grand_total = self.cost + tax
        print("The Grand XYZ Hotel")
        print("Name: ",self.name)
        print(f"Age: {self.age}")
        print(f"1 Day Cost: {one_day_cost}")
        print(f"{self.days} Stayed")
        print(f"Total Price {grand_total}")
        print("(Include all of the Taxes)")
        print("Thankyou For the Visit")




m = Management()
m.user_interface()