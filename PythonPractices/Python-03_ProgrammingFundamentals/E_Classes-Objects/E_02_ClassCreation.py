'''

EXAMPLE CLASS CREATION (just for notes)

1) DECLARATION
-------------------------------------------------------
    class ClassName:
-------------------------------------------------------

2) INSTERTION OF ATTRIBUTES
-------------------------------------------------------
    class ClassName:
        # Class attributes (shared by all instances)
        class_attribute = value
-------------------------------------------------------

3) CONSTRUCTOR METHOD [def int(self, attribute1,attribute2,...):]
     a) __init__  
            - method is a special method known as the constructor
            - initializes instance attributes (instance variables) when an object is created
     b) self
            - the first parameter of a constructor, referring to the instance being created
     c) attribute1, attribute2,...
            - parameters passed to the constructor when creating object
            - "self.attribute1", "self.attrbiute2", etc. ... are used to assign values to instance attributes

-------------------------------------------------------
    class ClassName:
        # Class attributes (shared by all instances)
        class.attribute = value

        # Constructor method (initialize instance attributes)
        def __init__(self, attribute1, attribute2,...):
            pass
            #....
-------------------------------------------------------

4) INSTANCE ATTRIBUTES (self.attribute1 = attribute1)
    - this is when we assign values to attributes
-------------------------------------------------------
    class ClassName:
        # Class attributes (shared by all instances)
        class.attribute = value

        # Constructor method (initialize instance attributes)
        def __init__(self, attribute1, attribute2,...):
            self.attribute1 = attribute1
            self.attribute2 = attribute2
            #....
-------------------------------------------------------

5) INSTANCE METHODS [def method(self, parameter1, parameter2,...)]
    - this is when we define the methods/functions within the class
    - they operate on the instance's data (attributes) and perform actions specific to instances
    
-------------------------------------------------------
    class ClassName:
        # Class attributes (shared by all instances)
        class.attribute = value

        # Constructor method (initialize instance attributes)
        def __init__(self, attribute1, attribute2,...):
            self.attribute1 = attribute1
            self.attribute2 = attribute2
            #....
        
        # Instance methods (functions)
        def method1(self, parameter1, parameter2, ...):
            # Method logic
            pass
        def method2(self, parameter1, parameter2, ...):
            # Method logic
            pass
-------------------------------------------------------

6) SUCCESSFULLY CREATED A CLASS!!!

'''