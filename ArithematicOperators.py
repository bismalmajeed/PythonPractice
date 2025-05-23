# Arithmetic Operators

# + - * / // % **

x = 10
y = 3

print("Addition : ", x + y)        # 10 + 3
print("Subtraction : ", x - y)     # 10 - 3
print("Multiplication: ", x * y)   # 10 * 3 = 30
print("Division : ", x / y)        # 10 / 3 = 3.33333
print("Floor Division: ", x // y)  # 10 // 3 = 3
print("Modulus : ", x % y)         # 10 % 3 = 1
print(x ** y)                      # 10 ** 3 = 10 * 10 * 10 = 1000

# Comparison Operators

x = 10
y = 50

print(x == y)   # 10 == 5  => False
print(x != y)   # 10 != 5  => True
print(x <= y)   # 10 <= 5  => True
print(x >= y)   # 10 <= 5  => False
print(y >= x)   # 50 > 10  => True
print(x > y)    # 10 > 50  => False
print(y < x)    # 50 < 10  => False
print(x < y)    # 10 < 10  => False


# Logical Operators
a = 10  
b = 15  
c = 25  

# Logical AND: Both conditions must be True
print(a > b and c > b)  # False (10>15 is False; 25>15 is True → False and True = False)
print(a < b and c > b)  # True (10<15 is True; 25>15 is True → True and True = True)

# Logical OR: At least one condition must be True
print(a > b or a > c)   # False (10>15 and 10>25 are both False → False or False = False)
print(a > b or c > b)   # True (25>15 is True → False or True = True)

# Logical NOT: Inverts the result
print(not(a > b))        # True (10>15 is False → not False = True)
print(not(a > b or c > b))  # False (a>borc>b is True → not True = False)


# Assignment Operator
x = 10  
y = x  # y = 10 (initial assignment)

x += 5  # Equivalent to x = x + 5 → 10 + 5 = 15
print(" add and assign : ", x)  # Output: 15

x -= 2  # Equivalent to x = x - 2 → 15 - 2 = 13
print(" subtract and assign : ", x)  # Output: 13

x *= 2  # Equivalent to x = x * 2 → 13 * 2 = 26
print(" multiply and assign : ", x)  # Output: 26

x /= 2  # Equivalent to x = x / 2 → 26 / 2 = 13.0 (result is a float)
print(" divide and assign : ", x)  # Output: 13.0

print(x)  # Final value of x: 13.0
print(y)  # y remains 10 (unaffected by changes to x)

""" Key Notes:
Membership operators (in and not in) check if a value exists (or does not exist) in a sequence like a list, string, or tuple.
The comment x=x*3 for x *= 2 is incorrect (typo). The correct calculation is 13 * 2 = 26.

Division (/) always returns a float in Python, even if the result is a whole number.

y retains its initial value (10) because assignment operators only modify the variable they act on.
"""


#Membership operator 
x = [1, 2, 5, 8, 22]

# Check if 3 exists in the list
print(3 in x)   # Output: False (3 is not in the list)

# Check if 5 exists in the list
print(5 in x)   # Output: True (5 is in the list)

# Check if 3 is NOT in the list
print(3 not in x)  # Output: True (3 is absent → "not in" is True)

# Check if 5 is NOT in the list
print(5 not in x)  # Output: False (5 is present → "not in" is False)

""" Key Notes:

in returns True if the value is found in the sequence.

not in returns True if the value is not found in the sequence.

These operators are case-sensitive and work with strings, tuples, dictionaries (checks keys), and other iterables.
"""


#identity  operator is, is not
a = "Hello"
b = "hello"
print(a is b)  # Output: False

"""
For small integers (e.g., -5 to 256), Python caches objects.

For interned strings (identical literals), Python may reuse objects.

Case Sensitivity: "Hello" and "hello" are different strings → different objects."""

