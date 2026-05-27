'''

EXAMPLE CLASS CREATION (just for notes)

1) CREATING OBJECTS (instances)
    - call the class like a function and provide arguments the constructor requires
    - each object is a distinct instance of the class, with its own instance attributes and the ability to call methods
-------------------------------------------------------
    # Create objects (instances of the class)
    object1 = ClassName(arg1, arg2, ...)
    object2 = ClassName(arg1, arg2, ...)
-------------------------------------------------------

2) CALLING METHODS ON OBJECTS
    - calling methods on objects: object1 and object2 in the example
    - method1 and method2 are defined in the ClassName class (see E_02_ClassCreation.py) 
    and we're calling them on object1 and object2 respectively

    2.A) METHOD1: DOT NOTATION
        - most straightforward way to call an object's method.
        - dot notation is: object.method()
    -------------------------------------------------------
    # Calling methods on objects
    # Method1: Using dot notation
    result1 = object1.method1(param1_value, param2_value, ...)
    result2 = object1.method1(param1_value, param2_value, ...)
    -------------------------------------------------------

    2.B) METHOD2: ASSIGNING OBJECT METHODS TO VARIABLES
        - assign the method reference to a varibale
        - "method_reference = object1.method1" assigns method1 of object1 to variable method_reference
        - after assigning, the method will be called using something like:
            result3 = method_reference(param1_value, param2_value, ...)
    -------------------------------------------------------
    # Calling methods on objects
    # Method2: Assigning object methods to variables
    method_reference = object1.method1  # Assign the method to a variable
    result3 = method_reference(param1_value, param2_value, ...)
    -------------------------------------------------------

3) ACCESSING OBJECT ATTRIBUTES
    - acessing an object's attribute using dot notation
    - "attribute_value = object1.attribute1" retrieves value of attribute1 from object1 and assigns it to 
    the variable "attribute_value"
-------------------------------------------------------
# Accessing object attributes
attribute_value = object1.attribute1  # Access the attribute using dot notation
-------------------------------------------------------

4) MODIFYING OBJECT ATTRIBUTES
    - by using dot notation
    - "object1.attribute2 = new_values" sets attribute2 of object1 to new_value
-------------------------------------------------------
# Modifying object attributes
object1.attribute2 = new_value  # Change the value of an attribute using dot notation
-------------------------------------------------------

5) ACCESSING CLASS ATTRIBUTES (shared by all instances)
    - "class_attr_value = ClassName.class_attribute" accesses the class attribute "class_attribute" from the
    ClassName "class" and assigns its value to the variable "class_attr_value"
-------------------------------------------------------
# Accessing class attributes (shared by all instances)
class_attr_value = ClassName.class_attribute
-------------------------------------------------------


'''