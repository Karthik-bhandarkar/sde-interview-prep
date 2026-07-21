"""
------------------------------------------------------------
Problem No : 08

Topic : While Loop

Pattern : Product Accumulator

Difficulty : ⭐⭐

Concepts Used :
- while loop
- Counter
- Accumulator
- User Input
- Multiplication

Objective :
Write a Python program to calculate the factorial
of a given number using a while loop.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

# Take input from the user
number = int(input("Enter the Number: "))

# Initialize variables
counter = number
product = 1

# Repeat until counter becomes 0
while counter >= 1:

    # Multiply the current counter value with product
    product *= counter

    # Decrease the counter by 1
    counter -= 1

# Display the final factorial
print(f"Factorial of {number} is: {product}")