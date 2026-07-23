"""
------------------------------------------------------------
Problem No : 14

Topic : While Loop

Pattern : Sum Accumulator

Difficulty : ⭐⭐⭐

Concepts Used :
- while loop
- Counter
- User Input
- Sum Accumulator

Objective :
Write a Python program to find the sum of
N user-entered numbers using a while loop.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

num = int(input("Enter How Many Number: "))
counter = 1
total = 0

while counter <= num:
    current_num = int(input("Enter The Number: "))
    total += current_num
    counter += 1
print(f"Sum of the {num} number is {total}")