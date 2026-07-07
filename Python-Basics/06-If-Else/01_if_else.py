"""
------------------------------------------------------------
Problem No : 01

Topic : If-Else

Problem : Positive, Negative or Zero

Difficulty : Easy

Concepts Used :
- input()
- int()
- if
- elif
- else

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
