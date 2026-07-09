# 06 - If-Else

Practice problems covering conditional statements in Python — `if`, `elif`, `else`, comparison operators, and the modulus operator. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | Positive, Negative or Zero | [`01_if_else.py`](./01_if_else.py) | Easy | `if` / `elif` / `else` |
| 02 | Even or Odd | [`02_even_or_odd.py`](./02_even_or_odd.py) | Easy | Modulus operator `%` |
| 03 | Voting Eligibility | [`03_voting_eligibility.py`](./03_voting_eligibility.py) | Easy | Comparison operator `>=` |
| 04 | Largest of Two Numbers | [`04_largest_of_two.py`](./04_largest_of_two.py) | Easy | Comparison operator `>` |
| 05 | Largest of Three Numbers | [`05_largest_of_three.py`](./05_largest_of_three.py) | Easy ⭐⭐⭐ | `and`, nested conditions |
| 08 | HackerRank - Python If-Else | [`08_hackerrank_python_if_else.py`](./08_hackerrank_python_if_else.py) | Easy | `if` / `elif` / `else`, Modulus `%` |
| 09 | GeeksforGeeks - If Conditional Statement | [`09_gfg_if_conditional_statement.py`](./09_gfg_if_conditional_statement.py) | Easy | Boolean values, `if`, `or`, `not` |

## 📝 Problem Details

### 01. Positive, Negative or Zero

Read an integer and print whether it is positive, negative, or zero.

```python
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
```

---

### 02. Even or Odd

Check whether a number is even or odd using the modulus operator.

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### 03. Voting Eligibility

Determine if a person is eligible to vote based on age (18+).

```python
age = int(input("Enter the Age of a Person: "))

if age >= 18:
    print("Person is Eligible to Vote")
else:
    print("Person is Not Eligible to Vote")
```

---

### 04. Largest of Two Numbers

Compare two numbers and print the larger one (or note if they're equal).

```python
number_1 = int(input("Enter the First Number: "))
number_2 = int(input("Enter the Second Number: "))

if number_1 > number_2:
    print(f"The largest number is {number_1}.")
elif number_1 == number_2:
    print("Both numbers are equal.")
else:
    print(f"The largest number is {number_2}.")
```

---

### 05. Largest of Three Numbers

Compare three numbers using chained `and` conditions to find the largest.

```python
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

if number_1 > number_2 and number_1 > number_3:
    print(f"The largest number is {number_1}.")
elif number_2 > number_1 and number_2 > number_3:
    print(f"The largest number is {number_2}.")
elif number_3 > number_1 and number_3 > number_2:
    print(f"The largest number is {number_3}.")
else:
    print("All three numbers are equal.")
```

---

### 08. HackerRank - Python If-Else

Solve HackerRank's introductory **Python If-Else** challenge by applying conditional statements (`if`, `elif`, and `else`) to determine whether a number is **"Weird"** or **"Not Weird"** based on the given rules.

**🔗 Problem Link:**  
https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

---

### 09. GeeksforGeeks - If Conditional Statement

Solve the GeeksforGeeks **If Conditional Statement** problem by implementing the `friends_in_trouble()` function.

Two friends, **John** and **Smith**, are represented by the boolean values:

- `j_angry`
- `s_angry`

Return **True** if:

- Both friends are angry.
- Neither friend is angry.

Otherwise, return **False**.

**🔗 Problem Link:**  
https://www.geeksforgeeks.org/problems/if-loop-python/1

---

## ▶️ How to Run

Each file is standalone. Run any of them with:

```bash
python3 01_if_else.py
```

You'll be prompted to enter input values in the terminal.

---

## 🎯 Key Takeaways

- `if` / `elif` / `else` statements allow programs to make decisions based on conditions.
- Conditions are evaluated from top to bottom until one evaluates to `True`.
- The modulus operator `%` is commonly used to determine whether a number is even or odd.
- Comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`) are the foundation of conditional logic.
- Logical operators (`and`, `or`, `not`) help combine multiple conditions into a single decision.
- Always consider edge cases such as equal values when comparing numbers.
- Practicing problems from **HackerRank** and **GeeksforGeeks** strengthens problem-solving skills and prepares you for coding interviews.

---

*Author: Karthik Bhandarkar*