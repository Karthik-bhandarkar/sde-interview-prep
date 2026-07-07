"""
------------------------------------------------------------
Problem No : 04
Topic      : Input & Type Conversion
Problem    : BMI Input
Difficulty : Easy

Question:
Take weight (kg) and height (m) as input and calculate BMI
using the formula: weight / (height ** 2).

Example Input:
70
1.75

Example Output:
Your BMI is: 22.86
------------------------------------------------------------
"""

# Solution
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))
