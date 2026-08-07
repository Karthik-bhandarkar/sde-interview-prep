"""
Problem: Student Marks Manager

Difficulty: Medium

Problem Statement:

You are given the following list of student marks:

marks = [45, 78, 90, 78, 56]

Perform the following operations in order:

1. Add a new student mark 88.
2. Insert the mark 60 at index 2.
3. Remove the first occurrence of mark 78.
4. Remove the last element.
5. Sort the marks in ascending order.
6. Reverse the list.
7. Print the index of mark 60.
8. Print how many times mark 78 appears.
9. Add another list [95, 100] to the existing list.
10. Print the final list.

Expected Skills:
- append()
- insert()
- remove()
- pop()
- sort()
- reverse()
- index()
- count()
- extend()

Concepts Used:
- Lists
- List Methods

Time Complexity:
O(n)
Space Complexity:
O(1)
"""

marks = [45, 78, 90, 78, 56]

# 1
marks.append(88)

# 2
marks.insert(2, 60)

# 3
marks.remove(78)

# 4
marks.pop()

# 5
marks.sort()

# 6
marks.reverse()

# 7
print("Index of 60:", marks.index(60))

# 8
print("Count of 78:", marks.count(78))

# 9
marks.extend([95, 100])

# 10
print("Final List:", marks)

#output 
Index of 60: 2
Count of 78: 1
Final List: [90, 78, 60, 56, 45, 95, 100]