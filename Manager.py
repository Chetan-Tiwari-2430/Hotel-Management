from Hotel import Hotel
class Manager:
    def show_available_rooms(self):
        hotel = Hotel()
        available_ac_rooms = hotel.available_ac_rooms()
        available_non_ac_rooms = hotel.available_non_ac_rooms()
        print(f"Available Ac Rooms: {available_ac_rooms}")
        print(f"Available Non Ac Rooms: {available_non_ac_rooms}")
        

