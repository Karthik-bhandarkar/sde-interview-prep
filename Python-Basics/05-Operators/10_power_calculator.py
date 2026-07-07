"""
------------------------------------------------------------
Problem No : 10
Topic      : Operators
Problem    : Power Calculator
Difficulty : Easy

Question:
Take a base number and an exponent as input and calculate the
result using the exponentiation operator (**).

Example Input:
2
10

Example Output:
Result: 1024.0
------------------------------------------------------------
"""

# Solution
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent: "))
result = base ** exponent
print("Result:", result)
