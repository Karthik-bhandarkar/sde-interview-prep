"""
------------------------------------------------------------
Problem No   : 02
Topic        : For Loop
Pattern      : Reverse Counter Pattern
Difficulty   : Easy
Concepts Used: for, range(), negative step
Objective    : Print numbers from 10 to 1 using a for loop.
Author       : Karthik Bhandarkar
------------------------------------------------------------
"""

"""
Problem Statement:
Write a Python program to print numbers from 10 to 1 in reverse order using a
for loop.

Example Output:
10
9
8
7
6
5
4
3
2
1

Constraints:
- Use only a for loop.
- Do not use a while loop.
- Use range() with a negative step.
"""

"""CODE"""
for i in range (10,0,-1):
    print(i)