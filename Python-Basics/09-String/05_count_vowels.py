"""
Problem: Count Vowels

Difficulty: Easy

Problem Statement:
Given a string s, count the total number of vowels present in the string.
Consider both uppercase and lowercase vowels.

Example:
Input:
Programming

Output:
3

Concepts Used:
- Direct Traversal
- if statement
- String Membership (in)
- Counter Pattern

Pattern:
- Counter Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

s = input()

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print(count)