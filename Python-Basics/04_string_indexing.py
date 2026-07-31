"""
Problem: Print Specific Characters

Difficulty: Easy

Problem Statement:
Given a string, print:

1. First character
2. Last character
3. Second character
4. Second last character

Example:

Input:
Python

Output:
P
n
y
o

Concepts Used:
- Positive Indexing
- Negative Indexing

Pattern:
- Indexing

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

s = input()

# Write your code here
print(s[0])
print(s[-1])
print(s[1])
print(s[-2])