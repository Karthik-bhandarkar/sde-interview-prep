"""
------------------------------------------------------------
Problem No : 12

Topic : While Loop

Pattern : Largest Accumulator

Difficulty : ⭐⭐⭐⭐

Concepts Used :
- while loop
- Counter
- User Input
- Comparison
- Largest Accumulator

Objective :
Write a Python program to find the largest number
among N user-entered numbers using a while loop.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

number = int(input("enter how much number u need: "))
counter  = 1

while counter <= number:
    current_number = int(input("Enter number: "))
    
    if counter == 1:
        largest  = current_number 

    if current_number >= largest:
        largest = current_number   
    
    counter += 1

print(largest)
