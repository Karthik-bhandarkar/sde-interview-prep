"""
------------------------------------------------------------
Problem No   : 08
Topic        : For Loop
Pattern      : ?
Difficulty   : Easy
Concepts Used: for, accumulator
Objective    : Find the factorial of a number.
Author       : Karthik Bhandarkar
------------------------------------------------------------
"""

"""
Problem Statement:

Write a Python program to find the factorial of 5.

Example:

5! = 5 × 4 × 3 × 2 × 1 = 120

Expected Output:
120

Constraints:
- Use a for loop.
- Do not use math.factorial().
"""

product = 1

for i in range(5,0,-1):
    product *= i
    
print(product)