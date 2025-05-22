

"""
class Calculator:
    num = 100  # Class variable

    def getData(self):
        print("I am now executing as method in class")  # Fixed indentation

# Create object
obj = Calculator()  # Correct syntax (no dot before parentheses)
obj.getData()        # Call method
print(obj.num)       # Access class variable


obj = Calculator() creates an instance of the Calculator class.

obj.getData() calls the method getData() and prints the message.

obj.num accesses the class variable num (shared across all instances).
"""

class Calculator:
    num = 100  # Class variable

    # Constructor (properly indented inside the class)
    def __init__(self, a, b):
        self.firstNumber = a  # Instance variable
        self.secondNumber = b  # Instance variable
        print("I am called automatically when object is created")

    # Method (properly indented inside the class)
    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


# Create an object (no "new" keyword)
obj = Calculator(5, 10)  # Pass values for `a` and `b`
obj.getData()  # Call method
print(obj.num)

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.num)

""" self: Mandatory first parameter for instance methods to access instance/class variables.

Constructor: Named __init__, automatically called during object creation.

Class vs. Instance Variables:

num = 100 is a class variable (shared across all instances).

"""

