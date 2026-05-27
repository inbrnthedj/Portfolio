'''
In this python program, a simple car class will be simulated:
    - create objects / car instances
    - accelerate cars
    - display current speeds

Class "Car" will have the following attributes and methods:
    - (ATTR)        :   max_speed = 120 km/h
    - (CONS. METHOD):   __init__ takes parameters:
        - make
        - model
        - color
        - speed (0 default)
    - (METHOD)      :   accelerate(self, acceleration)
        - allows car to accelerate
        - if acceleration does not exceed the "max_speed", update car's speed attribute. Otherwise
        set the speed to the max_speed.
    - (METHOD)      :   get_speed(self)
        - returns the current speed
'''
# CLASS CREATION
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
    

# OBJECTS CREATION

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# ACCELERATE THE CARS

# increase car1 by 30km/h and car2 by 20km/h
car1.accelerate(30)
car2.accelerate(20)

# DISPLAY CURRENT SPEED
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")


# If ran, it will print the new speed of the cars after the acceleration
