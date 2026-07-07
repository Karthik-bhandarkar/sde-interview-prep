"""
------------------------------------------------------------
Problem No : 09
Topic      : Operators
Problem    : Percentage
Difficulty : Easy

Question:
Take marks obtained and total marks as input, then calculate
and print the percentage using operators.

Example Input:
450
500

Example Output:
Percentage: 90.0
------------------------------------------------------------
"""

# Solution
marks_obtained = float(input("Enter marks obtained: "))
total_marks = float(input("Enter total marks: "))
percentage = (marks_obtained / total_marks) * 100
print("Percentage:", round(percentage, 2))
