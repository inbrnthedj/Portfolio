'''
This python code is a practice lab on creating classes and objects.
The class to be made is of rectangles with the following:
    - ATTRIBUTES: height, width, Color
    - ISTANCES: SkinnyBlueRectangle, FatYellowRectangle
    - METHODS: drawRectangle()
In order to draw the objects (the rectangles), matplot library will be imported

'''

# IMPORT LIBRARY
import matplotlib.pyplot as plt

# CREATE CLASS
class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# CREATE BLUE RECTANGLE
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')

# Print the object attributes
SkinnyBlueRectangle.height
SkinnyBlueRectangle.width
SkinnyBlueRectangle.color

# Draw the shape - opens a new window
SkinnyBlueRectangle.drawRectangle() # See Figure_3_SkinnyBlueRectangle.png

# CREATE BLUE RECTANGLE
FatYellowRectangle = Rectangle(20, 5, 'yellow')

# Print the object attributes
FatYellowRectangle.height 
FatYellowRectangle.width
FatYellowRectangle.color

# Draw the shape - opens a new window
FatYellowRectangle.drawRectangle() # See Figure_4_FatYellowRectangle.png