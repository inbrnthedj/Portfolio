'''
This python code is a practice lab on creating classes and objects.
The class to be made is of circles with the following:
    - ATTRIBUTES: radius, Color
    - ISTANCES: RedCircle, GreenCircle, YellowCircle
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