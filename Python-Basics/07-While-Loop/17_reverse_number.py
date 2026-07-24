"""
------------------------------------------------------------
Problem No : 17

Topic : While Loop

Pattern : Number Manipulation

Difficulty : ⭐⭐⭐⭐

Concepts Used :
- while loop
- Modulus Operator (%)
- Floor Division (//)
- Arithmetic Operations

Objective :
Write a Python program to reverse the digits
of a given integer using a while loop.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""
num = int(input("enter the number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse =  reverse * 10 + digit
    num = num // 10
print(reverse)

