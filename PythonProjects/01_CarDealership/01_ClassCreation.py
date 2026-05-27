'''
THIS PYTHON CODE AIMS TO:
1 - Represent vehicles using a class with attributes for maxspeed and mileage
2 - Update the class with the default color for all vehicles: "white"
3 - Create methods to assign seating capacity to a vehicle
4 - Create a method to display all the properties of an object of the class
5 - Create two objects of vehicle classwith:
    - Car1: Maxspeed 200kmph, mileage 20kmpl, 5 seating capacities
    - Car2: Maxspeed 180kmph, mileage 25kmpl, 4 seating capacities
'''

# 1 - CREATE CLASS WITH ATTRIBUTES
class Vehicle(object):
    # 2 - SET COLOR WHITE AS DEFAULT
    color="white" 

    # Constructor
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed 
        self.mileage = mileage
        self.seatingCapacity = None
    
    # 3 - METHOD FOR SEATING CAPACITY
    # Method
    def assignSeatingCapacity(self, seatingCapacity):
        self.seatingCapacity = seatingCapacity

    # 4 - METHOD TO PRINT PROPERTIES
    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.maxSpeed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seatingCapacity)

# 5 - CREATE TWO OBJECTS
# Creation with just attributes
Car1 = Vehicle(200, 20)
Car2 = Vehicle(180, 25)
# Adding seating capacities for each
Car1.assignSeatingCapacity(5)
Car2.assignSeatingCapacity(4)

# Print Attributes
Car1.display_properties()
Car2.display_properties()