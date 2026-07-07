"""
------------------------------------------------------------
Problem No : 05
Topic      : Operators
Problem    : Math Functions
Difficulty : Easy

Question:
Take a number as input and print its absolute value, square root,
and its power of 2 using built-in math functions.

Example Input:
-16

Example Output:
Absolute value: 16.0
Square root: 4.0
Power of 2: 256.0
------------------------------------------------------------
"""

# Solution
import math
num = float(input("Enter a number: "))
print("Absolute value:", abs(num))
print("Square root:", math.sqrt(abs(num)))
print("Power of 2:", num ** 2)
