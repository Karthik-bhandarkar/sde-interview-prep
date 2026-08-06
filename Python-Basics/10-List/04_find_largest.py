"""
Problem: Find Largest Element

Difficulty: Easy

Problem Statement:
Given a list of integers, find and print the largest element.

Example:
Input:
[10, 45, 7, 89, 23]

Output:
89

Concepts Used:
- List
- Direct Traversal
- if statement

Pattern:
- Maximum Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

numbers = [10, 45, 7, 89, 23]

# Write your code here
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest)