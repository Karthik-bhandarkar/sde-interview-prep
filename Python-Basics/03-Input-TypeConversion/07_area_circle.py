"""
------------------------------------------------------------
Problem No : 07
Topic      : Input & Type Conversion
Problem    : Area of Circle
Difficulty : Easy

Question:
Take the radius of a circle as input and calculate its area
using the formula: pi * r^2 (use 3.14159 for pi).

Example Input:
7

Example Output:
Area of Circle: 153.94
------------------------------------------------------------
"""

# Solution
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * (radius ** 2)
print("Area of Circle:", round(area, 2))
