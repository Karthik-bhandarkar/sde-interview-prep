"""
------------------------------------------------------------
Problem No : 02
Topic      : Operators
Problem    : Arithmetic Operations
Difficulty : Easy

Question:
Take two numbers as input and print the result of addition,
subtraction, multiplication, division, floor division, modulus,
and exponentiation.

Example Input:
10
3

Example Output:
Addition: 13.0
Subtraction: 7.0
Multiplication: 30.0
Division: 3.3333333333333335
Floor Division: 3.0
Modulus: 1.0
Exponentiation: 1000.0
------------------------------------------------------------
"""

# Solution
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
