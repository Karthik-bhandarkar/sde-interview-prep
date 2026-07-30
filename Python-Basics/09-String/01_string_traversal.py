"""
Problem: String Traversal

Difficulty: Easy

Problem Statement:
Given a string s, print each character of the string on a new line.

Example:
Input:
Python

Output:
P
y
t
h
o
n

Concepts Used:
- Strings
- for loop
- range()
- len()
- String Indexing

Pattern:
- Traversal Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

s = input()

# Write your code here
for i in range(len(s)):
    print(s[i])