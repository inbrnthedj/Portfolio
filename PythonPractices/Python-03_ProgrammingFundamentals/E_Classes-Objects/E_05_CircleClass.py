'''
This python code is a practice lab on creating classes and objects.
The class to be made is of circles with the following:
    - ATTRIBUTES: radius, Color
    - ISTANCES: RedCircle, BlueCircle
    - METHODS: add_radius(r), draw()
In order to draw the objects (the circle), matplot library will be imported

'''

# IMPORT LIBRARY
import matplotlib.pyplot as plt

# CREATE CLASS
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
dir(RedCircle)

# Print the object attribute radius
RedCircle.radius

# Print the object attribute color
RedCircle.color

# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius

# Call the method drawCircle - another window will appear
RedCircle.drawCircle() # See Figure_1_RedCircle.png

# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# ----- BLUE CIRCLE -----
# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)

# Print the object attributes
BlueCircle.radius
BlueCircle.color

# draw circle - another window will appear
BlueCircle.drawCircle() # See Figure_2_BlueCircle.png

