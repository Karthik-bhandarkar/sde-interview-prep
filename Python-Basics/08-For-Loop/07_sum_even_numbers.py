"""
------------------------------------------------------------
Problem No   : 07
Topic        : For Loop
Pattern      : ?
Difficulty   : Easy
Concepts Used: for, range(), accumulator
Objective    : Find the sum of even numbers from 2 to 20.
Author       : Karthik Bhandarkar
------------------------------------------------------------
"""

"""
Problem Statement:

Write a Python program to calculate and print the sum of all even numbers from
2 to 20.

Expected Output:
110

Constraints:
- Use a for loop.
- Do not use sum().
- Think about the most efficient range().
"""


total = 0 

for i in range(2,21,2):
    total+=i
print(total)