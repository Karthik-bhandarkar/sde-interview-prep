"""
------------------------------------------------------------
Problem No : 08
Topic      : Input & Type Conversion
Problem    : Simple Interest
Difficulty : Easy

Question:
Take principal, rate, and time as input and calculate the
simple interest.

Example Input:
10000
5
2

Example Output:
Simple Interest: 1000.0
------------------------------------------------------------
"""

# Solution
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)
