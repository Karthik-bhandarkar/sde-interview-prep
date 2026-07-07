"""
------------------------------------------------------------
Problem No : 10
Topic      : Input & Type Conversion
Problem    : Percentage Calculator
Difficulty : Easy

Question:
Take marks obtained in 5 subjects (out of 100 each) as input
and calculate the total and percentage.

Example Input:
80
90
75
85
95

Example Output:
Total Marks: 425.0
Percentage: 85.0
------------------------------------------------------------
"""

# Solution
m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))
m4 = float(input("Enter marks in subject 4: "))
m5 = float(input("Enter marks in subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
print("Total Marks:", total)
print("Percentage:", round(percentage, 2))
