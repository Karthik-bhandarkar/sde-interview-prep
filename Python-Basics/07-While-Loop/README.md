# 07 - While Loop

Practice problems covering `while` loops in Python, including counter patterns, reverse counters, and accumulators. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | Counter Pattern | [`01_counter_pattern.py`](./01_counter_pattern.py) | Easy ⭐ | `while`, increment `+=` |
| 02 | Reverse Counter Pattern | [`02_reverse_counter.py`](./02_reverse_counter.py) | Easy ⭐ | `while`, decrement `-=` |
| 03 | Even Numbers | [`03_even_numbers.py`](./03_even_numbers.py) | Easy ⭐ | `while`, increment by 2 |
| 04 | Odd Numbers | [`04_odd_numbers.py`](./04_odd_numbers.py) | Easy ⭐ | `while`, increment by 2 |
| 05 | Sum of Numbers (Accumulator) | [`05_sum_of_numbers.py`](./05_sum_of_numbers.py) | Easy ⭐⭐ | `while`, accumulator |
| 06 | Sum of Even Numbers | [`06_sum_of_even_numbers.py`](./06_sum_of_even_numbers.py) | Easy ⭐⭐ | `while`, accumulator, `+` |
| 07 | Product of Numbers | [`07_product_of_numbers.py`](./07_product_of_numbers.py) | Easy ⭐⭐ | `while`, product accumulator |
| 08 | Factorial | [`08_factorial.py`](./08_factorial.py) | Easy ⭐⭐ | `while`, product accumulator |
| 09 | Count Even Numbers | [`09_count_even_numbers.py`](./09_count_even_numbers.py) | Easy ⭐⭐ | `while`, count accumulator, `if` |
| 10 | Largest Number | [`10_largest_number.py`](./10_largest_number.py) | Easy ⭐⭐⭐ | `while`, comparison, `if` |

## 📝 Problem Details

### 01. Counter Pattern
Print numbers from 1 to 10 using a while loop.

```python
count = 1

while count <= 10:
    print(count)
    count += 1
```

---

### 02. Reverse Counter Pattern
Print numbers from 10 to 1 using a while loop.

```python
count = 10

while count >= 1:
    print(count)
    count -= 1
```

---

### 03. Even Numbers
Print all even numbers from 2 to 20 using a while loop.

```python
count = 2

while count <= 20:
    print(count)
    count += 2
```

---

### 04. Odd Numbers
Print all odd numbers from 1 to 19 using a while loop.

```python
count = 1

while count <= 19:
    print(count)
    count += 2
```

---

### 05. Sum of Numbers
Calculate the sum of numbers from 1 to 10 using a while loop.

```python
total = 0
count = 1

while count <= 10:
    total += count
    count += 1
print(total)
```

---

### 06. Sum of Even Numbers
Calculate the sum of all even numbers from 2 to 20.

```python
counter = 2
total = 0

while counter <= 20:
    total += counter
    counter += 2
print(total)
```

---

### 07. Product of Numbers
Calculate the product of numbers from 1 to 5.

```python
counter = 1
product = 1

while counter <= 5:
    product *= counter
    counter += 1

print(f"The product of numbers from 1 to 5 is: {product}")
```

---

### 08. Factorial
Calculate the factorial of a given number using a while loop.

```python
number = int(input("Enter the Number: "))
counter = number
product = 1

while counter >= 1:
    product *= counter
    counter -= 1

print(f"Factorial of {number} is: {product}")
```

---

### 09. Count Even Numbers
Count the total number of even numbers from 1 to a given number.

```python
number = int(input("enter the number:"))
counter = 1
count = 0

while counter <= number:
    if counter % 2 == 0:
        count += 1
    counter += 1

print(count)
```

---

### 10. Largest Number
Find the largest number from 1 to a given number using a while loop.

```python
number = int(input("Enter the limit number: "))
counter = 1
largest = 0

while counter <= number:
    if counter > largest:
        largest = counter
    counter += 1

print(f"The largest number from 1 to {number} is {largest}")
```

---

## ▶️ How to Run

Each file is standalone. Run any of them with:

```bash
python3 01_counter_pattern.py
```

---

## 🎯 Key Takeaways

- `while` loops execute a block of code repeatedly as long as the condition is `True`.
- A **counter variable** must be initialized before the loop and updated (incremented or decremented) inside the loop to avoid an infinite loop.
- The **Accumulator Pattern** (`total += count`) is commonly used to find sums, products, or string concatenations inside loops.
- `+=`, `-=`, `*=`, and `/=` are compound assignment operators that simplify updating variable values.

---

*Author: Karthik Bhandarkar*
