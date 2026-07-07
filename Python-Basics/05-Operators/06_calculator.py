"""
------------------------------------------------------------
Problem No : 06
Topic      : Operators
Problem    : Calculator
Difficulty : Easy

Question:
Take two numbers as input and print the result of all four basic
operations on them (+, -, *, /). No if-else yet, so all results
are shown together.

Example Input:
20
4

Example Output:
Addition Result: 24.0
Subtraction Result: 16.0
Multiplication Result: 80.0
Division Result: 5.0
------------------------------------------------------------
"""

# Solution
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition Result:", num1 + num2)
print("Subtraction Result:", num1 - num2)
print("Multiplication Result:", num1 * num2)
print("Division Result:", num1 / num2)
