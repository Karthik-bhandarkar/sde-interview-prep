# 08 - For Loop

Practice problems covering `for` loops, `range()` parameter variations (start, stop, step), reverse loops with negative steps, accumulator patterns, and mathematical applications. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | Counter Pattern | [`01_counter_pattern.py`](./01_counter_pattern.py) | Easy ⭐ | `for`, `range(start, stop)` |
| 02 | Reverse Counter Pattern | [`02_reverse_counter_pattern.py`](./02_reverse_counter_pattern.py) | Easy ⭐ | `for`, `range()` with negative step `-1` |
| 03 | Even Numbers | [`03_even_numbers.py`](./03_even_numbers.py) | Easy ⭐ | `for`, `range()` step value `2` |
| 04 | Odd Numbers | [`04_odd_numbers.py`](./04_odd_numbers.py) | Easy ⭐ | `for`, `range(1, 20, 2)` |
| 05 | Multiples of 5 | [`05_multiples_of_5.py`](./05_multiples_of_5.py) | Easy ⭐ | `for`, `range(5, 51, 5)` |
| 06 | Sum 1 to 10 | [`06_sum_1_to_10.py`](./06_sum_1_to_10.py) | Easy ⭐⭐ | `for`, sum accumulator pattern |
| 07 | Sum of Even Numbers | [`07_sum_even_numbers.py`](./07_sum_even_numbers.py) | Easy ⭐⭐ | `for`, even step accumulator |
| 08 | Factorial | [`08_factorial.py`](./08_factorial.py) | Easy ⭐⭐ | `for`, product accumulator, reverse step |
| 09 | Multiplication Table | [`09_multiplication_table.py`](./09_multiplication_table.py) | Easy ⭐⭐ | `for`, dynamic input, `n * i` |

---

## 📝 Problem Details

### 01. Counter Pattern
Print numbers from 1 to 10 using a `for` loop and `range()`.

```python
for i in range(1, 11):
    print(i)
```

---

### 02. Reverse Counter Pattern
Print numbers from 10 to 1 in reverse order using a negative step in `range()`.

```python
for i in range(10, 0, -1):
    print(i)
```

---

### 03. Even Numbers
Print all even numbers from 2 to 20 without using conditional `if` statements.

```python
for i in range(2, 21, 2):
    print(i)
```

---

### 04. Odd Numbers
Print all odd numbers from 1 to 19 using `range()` with step value 2.

```python
for i in range(1, 20, 2):
    print(i)
```

---

### 05. Multiples of 5
Print all multiples of 5 from 5 up to 50.

```python
for i in range(5, 51, 5):
    print(i)
```

---

### 06. Sum 1 to 10
Calculate the total sum of integers from 1 to 10 using an accumulator variable.

```python
total = 0

for i in range(1, 11):
    total += i

print(total)
```

---

### 07. Sum of Even Numbers
Calculate the sum of all even numbers from 2 to 20 efficiently using step value `2`.

```python
total = 0

for i in range(2, 21, 2):
    total += i

print(total)
```

---

### 08. Factorial
Calculate the factorial of 5 ($5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$) using a product accumulator.

```python
product = 1

for i in range(5, 0, -1):
    product *= i

print(product)
```

---

### 09. Multiplication Table
Print the multiplication table (1 to 10) for any input number $n$.

```python
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n * i)
```

---

## ▶️ How to Run

```bash
python 01_counter_pattern.py
```

---

## 🎯 Key Takeaways

- `range(start, stop, step)` generates sequence of numbers:
  - `start` is inclusive.
  - `stop` is **exclusive**.
  - `step` defines increment/decrement.
- **Negative Step** (`range(10, 0, -1)`) iterates backwards.
- Accumulator pattern (`total += i` or `product *= i`) keeps running counts inside deterministic loops.

---

*Author: Karthik Bhandarkar*
