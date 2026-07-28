"""
------------------------------------------------------------
Problem No   : 03
Topic        : For Loop
Pattern      : Step Pattern
Difficulty   : Easy
Concepts Used: for, range(), step value
Objective    : Print even numbers from 2 to 20 using a for loop.
Author       : Karthik Bhandarkar
------------------------------------------------------------
"""

"""
Problem Statement:
Write a Python program to print all even numbers from 2 to 20 using a
for loop.

Example Output:
2
4
6
8
10
12
14
16
18
20

Constraints:
- Use only a for loop.
- Do not use an if statement.
- Use range() with an appropriate step value.
"""

"""
CODE
"""
for i in range(2,21,2):
    print(i)