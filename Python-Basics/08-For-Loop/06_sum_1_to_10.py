"""
------------------------------------------------------------
Problem No   : 06
Topic        : For Loop
Pattern      : ?
Difficulty   : Easy
Concepts Used: for, range(), accumulator
Objective    : Find the sum of numbers from 1 to 10.
Author       : Karthik Bhandarkar
------------------------------------------------------------
"""

"""
Problem Statement:

Write a Python program to calculate and print the sum of numbers from 1 to 10.

Expected Output:
55

Constraints:
- Use a for loop.
- Do not use Python's built-in sum() function.
"""


total =0 

for i in range(1,11):
    total+=i
print(total)
