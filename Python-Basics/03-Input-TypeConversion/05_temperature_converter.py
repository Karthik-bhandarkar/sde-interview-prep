"""
------------------------------------------------------------
Problem No : 05
Topic      : Input & Type Conversion
Problem    : Temperature Converter
Difficulty : Easy

Question:
Take temperature in Celsius as input and convert it to
Fahrenheit using the formula: (C * 9/5) + 32.

Example Input:
37

Example Output:
Temperature in Fahrenheit: 98.6
------------------------------------------------------------
"""

# Solution
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
