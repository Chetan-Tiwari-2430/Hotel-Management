class Management:
    cost = 0
    days = 0
    name = None
    age = None
    def user_interface(self):
        print("The Grand XYZ Hotel")
        print("1. Book Room")
        print("2. Show the Price")
        print("0. Exit")
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1:
                self.book_room()
            case 2:
                self.show_room_prices()
            case 0:
                return
            case _:
                print("Enter only 0 to 2")
    



    def book_room(self):
        print("1. For Ac rooms")
        print("2. For Non-Ac rooms")
        choice = int(input("Enter Your choice: "))
        if (choice in (1,2)):
            self.allocation(choice)
        
    
    def allocation(self,choice):
        if choice == 1:
            self.ac_room_booking()
        else:
            self.non_ac_room_booking()


    def ac_room_booking(self):
        self.name = input("Enter Your Name: ")
        self.age = int(input("Enter Your Age: "))
        self.days = int(input("How Many days you have to stay: "))
        fair_for_one_day = 1000
        print("Room Booked Successful")
        self.cost =  int(self.days*fair_for_one_day)
        self.bill()

    def non_ac_room_booking(self):
        self.name = input("Enter Your Name: ")
        self.age = int(input("Enter Your Age: "))
        self.days = int(input("How Many days you have to stay: "))
        fair_for_one_day = 800
        print("Room Booked Successful")
        self.cost =  int(self.days*fair_for_one_day)
        self.bill()


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