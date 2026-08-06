"""
Problem: Find Smallest Element

Difficulty: Easy

Problem Statement:
Given a list of integers, find and print the smallest element.

Example:
Input:
[10, 45, 7, 89, 23]

Output:
7

Concepts Used:
- List
- Direct Traversal
- if statement

Pattern:
- Minimum Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

numbers = [10, 45, 7, 89, 23]

# Write your code here
smallest = numbers[0]

for n in numbers:

    if n < smallest:

        smallest = n
        
print(smallest)