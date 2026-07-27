# 07 - While Loop

Practice problems covering `while` loops in Python, including counter patterns, reverse counters, accumulators, number manipulation, and more. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

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
| 10 | Largest Number (1 to N) | [`10_largest_number.py`](./10_largest_number.py) | Easy ⭐⭐⭐ | `while`, comparison, `if` |
| 11 | Smallest Number (1 to N) | [`11_smallest_number.py`](./11_smallest_number.py) | Easy ⭐⭐⭐ | `while`, comparison, `if` |
| 12 | Largest of N Numbers | [`12_largest_number.py`](./12_largest_number.py) | Medium ⭐⭐⭐⭐ | `while`, user input, comparison |
| 13 | Smallest of N Numbers | [`13_smallest_number.py`](./13_smallest_number.py) | Medium ⭐⭐⭐⭐ | `while`, user input, comparison |
| 14 | Sum of N Numbers | [`14_sum_of_n_numbers.py`](./14_sum_of_n_numbers.py) | Medium ⭐⭐⭐ | `while`, user input, sum accumulator |
| 15 | Average of N Numbers | [`15_average_of_n_numbers.py`](./15_average_of_n_numbers.py) | Medium ⭐⭐⭐ | `while`, user input, average |
| 16 | Count Positive / Negative / Zero | [`16_count_positive_negative_zero.py`](./16_count_positive_negative_zero.py) | Medium ⭐⭐⭐⭐ | `while`, `if/elif/else`, counters |
| 17 | Reverse a Number | [`17_reverse_number.py`](./17_reverse_number.py) | Medium ⭐⭐⭐⭐ | `while`, `%`, `//`, digit extraction |
| 18 | Palindrome Number | [`18_palindrome_number.py`](./18_palindrome_number.py) | Medium ⭐⭐⭐⭐ | `while`, `%`, `//`, reverse, compare |

---

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

### 10. Largest Number (1 to N)
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

### 11. Smallest Number (1 to N)
Find the smallest number from 1 to a given number using a while loop.

```python
number = int(input("Enter The Limit Number: "))
counter = 1
smallest = 1

while counter <= number:
    if counter < smallest:
        smallest = counter
    counter += 1
print(f"The smallest number from 1 to {number} is {smallest}")
```

---

### 12. Largest of N Numbers
Find the largest number among N user-entered numbers using a while loop.

```python
number = int(input("enter how much number u need: "))
counter = 1

while counter <= number:
    current_number = int(input("Enter number: "))

    if counter == 1:
        largest = current_number

    if current_number >= largest:
        largest = current_number

    counter += 1

print(largest)
```

---

### 13. Smallest of N Numbers
Find the smallest number among N user-entered numbers using a while loop.

```python
num = int(input("Enter how many number: "))
counter = 1

while counter <= num:
    current_num = int(input("Enter The Number: "))

    if counter == 1:
        smallest = current_num

    if current_num <= smallest:
        smallest = current_num

    counter += 1

print(smallest)
```

---

### 14. Sum of N Numbers
Calculate the sum of N user-entered numbers using a while loop.

```python
num = int(input("Enter How Many Number: "))
counter = 1
total = 0

while counter <= num:
    current_num = int(input("Enter The Number: "))
    total += current_num
    counter += 1

print(f"Sum of the {num} number is {total}")
```

---

### 15. Average of N Numbers
Calculate the average of N user-entered numbers using a while loop.

```python
num = int(input("Enter How Many Number: "))
counter = 1
total = 0

while counter <= num:
    current_num = int(input("Enter The Number: "))
    total += current_num
    counter += 1

avg = total / num
print(avg)
```

---

### 16. Count Positive / Negative / Zero
Count how many of the N user-entered numbers are positive, negative, or zero.

```python
num = int(input("enter the how many number: "))
positive = 0
negative = 0
zero = 0
counter = 1

while counter <= num:
    current_num = int(input("Enter the number: "))

    if current_num > 0:
        positive += 1
    elif current_num < 0:
        negative += 1
    else:
        zero += 1

    counter += 1

print(f"Positive Numbers : {positive}")
print(f"Negative Numbers : {negative}")
print(f"Zeroes           : {zero}")
```

---

### 17. Reverse a Number
Reverse the digits of a given integer using a while loop.

```python
num = int(input("enter the number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)
```

> **How it works:** On each iteration, the last digit is extracted with `% 10`, appended to `reverse` by shifting left (`* 10 + digit`), then removed from `num` with `// 10`.

---

### 18. Palindrome Number
Check whether a given number is a palindrome using a while loop.

```python
num = int(input("Enter the number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
```

> **How it works:** The original number is saved before reversing. After the loop, if the reversed number equals the original, it is a palindrome (e.g. `121`, `1331`).

---

## ▶️ How to Run

Each file is standalone. Run any of them with:

```bash
python 01_counter_pattern.py
```

---

## 🎯 Key Takeaways

- `while` loops execute a block of code repeatedly as long as the condition is `True`.
- A **counter variable** must be initialized before the loop and updated (incremented or decremented) inside the loop to avoid an infinite loop.
- The **Accumulator Pattern** (`total += count`) is commonly used to find sums, products, or counts inside loops.
- `+=`, `-=`, `*=`, and `/=` are compound assignment operators that simplify updating variable values.
- **Digit Extraction** using `% 10` and `// 10` is a powerful technique to process individual digits of a number.
- Always **save the original value** before modifying a variable (e.g., palindrome check).

---

*Author: Karthik Bhandarkar*
