"""
------------------------------------------------------------
Problem No   : 04
Topic        : For Loop
Pattern      : Step Pattern
Difficulty   : Easy
Concepts Used: for, range(), step value
Objective    : Print odd numbers from 1 to 19 using a for loop.
Author       : Karthik Bhandarkar
------------------------------------------------------------
"""

"""
Problem Statement:
Write a Python program to print all odd numbers from 1 to 19 using a
for loop.

Example Output:
1
3
5
7
9
11
13
15
17
19

Constraints:
- Use only a for loop.
- Do not use an if statement.
- Use range() with an appropriate step value.
"""

for i in range (1,20,2):
    print(i)