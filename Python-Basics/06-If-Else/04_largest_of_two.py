"""
------------------------------------------------------------
Problem No : 04

Topic : If-Else

Problem : Largest of Two Numbers

Difficulty : Easy

Concepts Used :
- input()
- int()
- if
- else
- Comparison Operator (>)

Objective :
Write a program to determine the largest among two numbers.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""
number_1 = int(input("Enter the First Number:"))
number_2 = int(input("Enter the Second Number:"))

if number_1 > number_2:
    print(f"The largest number is {number_1}.")
elif number_1 == number_2:
    print("Bothe Number or Equal")
else:
    print(f"The largest number is {number_2}.")