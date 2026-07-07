"""
------------------------------------------------------------
Problem No : 03
Topic      : Strings
Problem    : String Slicing
Difficulty : Easy

Question:
Create a string and print the first 3 characters, the last 3
characters, and a fully reversed version of it using slicing.

Example Output:
First 3 characters: Pyt
Last 3 characters: ing
Reversed string: gnimmargorP nohtyP
------------------------------------------------------------
"""

# Solution
text = "Python Programming"
print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Reversed string:", text[::-1])
