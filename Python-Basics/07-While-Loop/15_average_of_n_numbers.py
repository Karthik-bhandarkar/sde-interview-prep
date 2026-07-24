"""
------------------------------------------------------------
Problem No : 15

Topic : While Loop

Pattern : Average Accumulator

Difficulty : ⭐⭐⭐

Concepts Used :
- while loop
- Counter
- User Input
- Sum Accumulator
- Arithmetic Operator (/)

Objective :
Write a Python program to find the average of
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

avg = total/num
print(avg)