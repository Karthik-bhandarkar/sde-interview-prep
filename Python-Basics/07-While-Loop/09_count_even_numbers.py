"""
------------------------------------------------------------
Problem No : 09

Topic : While Loop

Pattern : Count Accumulator

Difficulty : ⭐⭐

Concepts Used :
- while loop
- Counter
- Accumulator
- User Input
- if statement

Objective :
Write a Python program to count the total number
of even numbers from 1 to a given number.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""
number= int(input("enter the number:"))
counter = 1
count = 0

while counter <= number:
    if counter % 2 == 0:
        count += 1
    counter += 1

print(count)