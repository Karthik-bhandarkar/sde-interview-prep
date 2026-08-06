"""
Problem: Sum of List Elements

Difficulty: Easy

Problem Statement:
Given a list of integers, print the sum of all elements.

Example:
Input:
[10, 20, 30, 40]

Output:
100

Concepts Used:
- List
- Direct Traversal
- Accumulator Pattern

Pattern:
- Accumulator Pattern

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

numbers = [10, 20, 30, 40]

# Write your code here
total = 0


for num in numbers:
    total+= num
  
print(total)