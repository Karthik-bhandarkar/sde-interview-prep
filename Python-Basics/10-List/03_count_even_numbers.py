"""
Problem: Count Even Numbers

Difficulty: Easy

Problem Statement:
Given a list of integers, count how many even numbers are present.

Example:
Input:
[10, 15, 20, 25, 30]

Output:
3

Concepts Used:
- List
- Direct Traversal
- if statement
- Modulus Operator (%)

Pattern:
- Counter Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

numbers = [10, 15, 20, 25, 30]

# Write your code here

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(count)