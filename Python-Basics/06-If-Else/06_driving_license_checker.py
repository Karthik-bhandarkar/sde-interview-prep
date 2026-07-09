"""
------------------------------------------------------------
Problem No : 06

Topic : Nested If

Problem : Driving License Checker

Difficulty : Easy ⭐⭐

Concepts Used :
- input()
- int()
- if
- Nested if

Objective :
Write a program to check whether a person is allowed to drive.

Author : Karthik Bhandarkar
------------------------------------------------------------
"""

# Ask the user to enter their age
age = int(input("Enter your age: "))

# First condition: Check if the person is 18 or older
if age >= 18:

    # Only if age is 18 or above, ask about the driving license
    has_license = input("Do you have a driving license? (yes/no): ").lower()

    # Second condition: Check if the user has a license
    if has_license == "yes":
        print("You are allowed to drive.")
    else:
        print("Apply for a driving license.")

# If age is below 18
else:
    print("You are not eligible to drive.")