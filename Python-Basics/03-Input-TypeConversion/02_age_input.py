"""
------------------------------------------------------------
Problem No : 02
Topic      : Input & Type Conversion
Problem    : Age Input
Difficulty : Easy

Question:
Take the user's age as input (input() always returns a string),
convert it to an integer, and print their age 10 years from now.

Example Input:
21

Example Output:
In 10 years, you will be 31 years old.
------------------------------------------------------------
"""

# Solution
age = int(input("Enter your age: "))
print("In 10 years, you will be", age + 10, "years old.")
