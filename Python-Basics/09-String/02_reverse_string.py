"""
Problem: Reverse String

Difficulty: Easy

Problem Statement:
Given a string s, print the characters of the string in reverse order.

Example:
Input:
Python

Output:
nohtyP

Concepts Used:
- Strings
- Reverse Traversal
- range()
- len()
- String Indexing
- print(end="")

Pattern:
- Reverse Traversal Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

s = input()

# Write your code here
last_index = len(s) - 1

for i in range(last_index, -1, -1):
    print(s[i], end = "")
    