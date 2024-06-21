"""Parking Lot Challenge:
Create a parking lot class that takes in a square footage size as input and creates an array of
empty values based on the input square footage size. Assume every parking spot is 8x12 (96 ft2)
for this program, but have the algorithm that calculates the array size be able to account for
different parking spot sizes. For example, a parking lot of size 2000ft2 can fit 20 cars, but if the
parking spots were 10x12 (120 ft2), it could only fit 16 cars. The size of the array will determine
how many cars can fit in the parking lot.

Parking_lot.py



# This program simulates a parking lot where cars with 7-digit license plates can park in random spots.
# The ParkingLot class initializes a parking lot of a given size with a specified parking spot size.
# The Car class represents a car with a license plate and methods to park the car in the parking lot.
# The main function simulates the process of parking a list of cars in random spots until the parking lot is full."""

import random

class ParkingLot:
    def __init__(self, size_in_sqft, spot_length=8, spot_width=12):
        """
        Initialize the parking lot with a given size and spot dimensions.
        Calculates the number of spots based on the size and spot dimensions.
        """
        self.spot_size = spot_length * spot_width
        self.num_spots = size_in_sqft // self.spot_size
        self.spots = [None] * self.num_spots
        
        if self.spot_size > size_in_sqft:
            raise ValueError("spot_size cannot be more than size_in_sqft.")

    def is_full(self):
        """
        Check if the parking lot is full.
        Returns True if there are no empty spots, False otherwise.
        """
        for spot in self.spots:
            if spot is None:
                return False
        return True

    def find_random_empty_spot(self):
        """
        Find a random empty spot in the parking lot.
        Returns the index of an empty spot, or None if the lot is full.
        """
        empty_spots = [i for i, spot in enumerate(self.spots) if spot is None]
        return random.choice(empty_spots) if empty_spots else None
        

class Car:
    def __init__(self, license_plate):
        """
        Initialize the car with a given license plate.
        Raises a ValueError if the license plate is not a 7 digit alphanumeric string.
        """
        if len(license_plate) != 7 or not license_plate.isalnum():
            raise ValueError("License plate must be a 7 digit alphanumeric string.")
        self.license_plate = license_plate

    def __str__(self):
        """
        Return the license plate as the string representation of the car.
        """
        return self.license_plate

    def park(self, parking_lot, spot_number):
        """
        Attempt to park the car in the given spot number of the parking lot.
        Returns a tuple (success, message) indicating whether the parking was successful and a message.
        """
        if spot_number < 0 or spot_number >= parking_lot.num_spots:
            return False, f"Spot number {spot_number} is out of range."
            
        if parking_lot.spots[spot_number] is None:
            parking_lot.spots[spot_number] = self
            return True, f"Car with license plate {self.license_plate} parked successfully in spot {spot_number}."
        else:
            return False, f"Spot {spot_number} is already occupied."
            

def main(cars, parking_lot):
    """
    Simulate parking each car in the list of cars into random spots in the parking lot.
    Continues until all cars are parked or the parking lot is full.
    At the end, save the mapping of vehicles to spots in a JSON file and upload it to an S3 bucket.
    """
    for car in cars:
        if parking_lot.is_full():
            print("Parking lot is full. Exiting program.")
            break
        
        while True:
            spot_number = parking_lot.find_random_empty_spot()
            if spot_number is None:
                print("Parking lot is full. Exiting program.")
                break
            success, message = car.park(parking_lot, spot_number)
            print(message)
            if success:
                break
    

if __name__ == "__main__":
    # Example usage: Create a parking lot and a list of cars, then try to park them.
    size_sft = int(input("Enter the size of the parking lot in square feet: "))
    spot_length = int(input("Enter the length of each parking spot in feet: "))
    spot_width = int(input("Enter the width of each parking spot in feet: "))
    parking_lot = ParkingLot(size_in_sqft=size_sft, spot_length=spot_length, spot_width=spot_width)
    
    cars = [Car("ABC 1234"), Car("XYZ567890"), Car("!LMN3456"), Car("QWE7890"),Car("DBC1234"), Car("WYZ5678"), Car("OMN3456"), Car("PWE7890"),Car("EBC1234"), Car("QYZ5678"), Car("JMN3456")]
    #cars = [Car("".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=7))) for _ in range(parking_lot.num_spots)]

    main(cars, parking_lot)









