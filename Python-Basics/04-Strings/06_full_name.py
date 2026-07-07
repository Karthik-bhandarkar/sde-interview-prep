"""
------------------------------------------------------------
Problem No : 06
Topic      : Strings
Problem    : Full Name
Difficulty : Easy

Question:
Take first name and last name as input and combine them into
a full name using string concatenation.

Example Input:
Karthik
Bhandarkar

Example Output:
Full Name: Karthik Bhandarkar
------------------------------------------------------------
"""

# Solution
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Full Name:", full_name)
