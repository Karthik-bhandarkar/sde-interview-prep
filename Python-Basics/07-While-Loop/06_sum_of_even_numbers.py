"""
------------------------------------------------------------
Problem No : 06

Topic : While Loop

Pattern : Accumulator Pattern

Difficulty : ⭐⭐

Concepts Used :
- while
- Counter
- Accumulator
- Arithmetic Operator (+)

Objective :
Calculate the sum of all even numbers from 2 to 20.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

counter = 2
total = 0

while counter <= 20:
    total += counter
    counter += 2
print(total)