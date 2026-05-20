'''AttributeError'''
# an attribute or method is accessed on an object that doesn't possess that sepcific attribute or method
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError