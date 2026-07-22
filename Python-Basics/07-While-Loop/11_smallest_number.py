"""
------------------------------------------------------------
Problem No : 11

Topic : While Loop

Pattern : Smallest Accumulator

Difficulty : ⭐⭐⭐

Concepts Used :
- while loop
- Counter
- Comparison
- if statement
- Smallest Accumulator

Objective :
Write a Python program to find the smallest number
from 1 to a given number using a while loop.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

number = int(input("Enter The Limit Number: "))
counter = 1
smallest = 1

while counter <= number:
    if counter < smallest:
        smallest = counter
    counter += 1
print(f"The smallest number from 1 to {number} is {smallest}")