"""
------------------------------------------------------------
Problem No : 16

Topic : While Loop

Pattern : Counter Pattern

Difficulty : ⭐⭐⭐⭐

Concepts Used :
- while loop
- Counter
- if / elif / else
- User Input

Objective :
Write a Python program to count positive,
negative, and zero values entered by the user.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

num = int(input("enter the how many number: "))
postive = 0
negative = 0
zero = 0 
counter = 1
while counter <= num:
    current_num = int(input("Enter the number: "))
    
    if current_num > 0:
        postive += 1
    elif current_num < 0:
        negative += 1
    else:
        zero +=1
    counter += 1

print(f"Positive Numbers : {positive}")
print(f"Negative Numbers : {negative}")
print(f"Zeroes           : {zero}")