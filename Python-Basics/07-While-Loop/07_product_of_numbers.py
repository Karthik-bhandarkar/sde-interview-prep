"""
------------------------------------------------------------
Problem No : 07

Topic : While Loop

Pattern : Product Accumulator

Difficulty : ⭐⭐

Concepts Used :
- while
- Counter
- Accumulator
- Multiplication

Objective :
Calculate the product of numbers from 1 to 5.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

counter = 1
product = 1

while counter <= 5:
    product *= counter
    counter += 1

print(f"The product of numbers from 1 to 5 is: {product}")