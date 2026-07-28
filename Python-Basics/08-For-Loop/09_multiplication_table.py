"""
Problem: Multiplication Table

Difficulty: Easy

Problem Statement:
Given a number n, print the multiplication table of n from 1 to 10.

Example:
Input:
9

Output:
9 18 27 36 45 54 63 72 81 90

Concepts Used:
- for loop
- range()
- Arithmetic Operators (*)

Pattern:
- Counter Pattern

Time Complexity:
O(10) ≈ O(1)

Space Complexity:
O(1)
"""

n = int(input())

for i in range(1, 11):
    print(n * i)