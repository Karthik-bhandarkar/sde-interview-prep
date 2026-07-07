"""
------------------------------------------------------------
Problem No : 03

Topic : If-Else

Problem : Voting Eligibility

Difficulty : Easy

Concepts Used :
- input()
- int()
- if
- else
- Comparison Operator (>=)

Objective :
Write a program to determine whether a person is eligible to vote based on their age.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

age = int(input("Enter the Age of a Person:"))

if age >= 18:
    print("Person is Eligible to vote")
else:
    print("person is not Eligible to vote")
