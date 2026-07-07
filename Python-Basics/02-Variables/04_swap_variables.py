"""
------------------------------------------------------------
Problem No : 04
Topic      : Variables
Problem    : Swap Variables
Difficulty : Easy

Question:
Swap the values of two variables a and b WITHOUT using a third
variable, and print both before and after swapping.

Example Output:
Before swap -> a: 5 , b: 10
After swap  -> a: 10 , b: 5
------------------------------------------------------------
"""

# Solution
a = 5
b = 10
print("Before swap -> a:", a, ", b:", b)
a, b = b, a
print("After swap  -> a:", a, ", b:", b)
