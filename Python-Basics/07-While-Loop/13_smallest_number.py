"""
------------------------------------------------------------
Problem No : 13

Topic : While Loop

Pattern : Smallest Accumulator

Difficulty : ⭐⭐⭐⭐

Concepts Used :
- while loop
- Counter
- User Input
- Comparison
- Smallest Accumulator

Objective :
Write a Python program to find the smallest number
among N user-entered numbers using a while loop.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

num = int (input("Enter how many number: "))
counter = 1

while counter <= num:
    current_num =  int(input("Enter The Number: "))

    if counter == 1:
        smallest = current_num

    if current_num <= smallest:
        smallest = current_num
    
    counter +=1
print(smallest)