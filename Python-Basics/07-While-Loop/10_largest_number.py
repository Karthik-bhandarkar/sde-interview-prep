"""
------------------------------------------------------------
Problem No : 10

Topic : While Loop

Pattern : Largest Number

Difficulty : ⭐⭐⭐

Concepts Used :
- while loop
- Counter
- Comparison
- if statement
- Largest Accumulator

Objective :
Write a Python program to find the largest number
from 1 to a given number using a while loop.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

number = int(input("Enter the limit number: "))
counter = 1
largest = 0

while counter <= number:
    if counter > largest:
        largest = counter
    counter += 1

print(f"The largest number from 1 to {number} is {largest}")