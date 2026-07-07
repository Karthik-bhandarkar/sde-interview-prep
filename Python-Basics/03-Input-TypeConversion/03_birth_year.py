"""
------------------------------------------------------------
Problem No : 03
Topic      : Input & Type Conversion
Problem    : Birth Year
Difficulty : Easy

Question:
Take the current year and the user's age as input, then
calculate and print the user's birth year.

Example Input:
2026
21

Example Output:
Your birth year is: 2005
------------------------------------------------------------
"""

# Solution
current_year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))
birth_year = current_year - age
print("Your birth year is:", birth_year)
