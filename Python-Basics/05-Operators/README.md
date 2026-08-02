# 05 - Operators

Practice problems covering arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`), operator precedence (PEMDAS/BODMAS), augmented assignment (`+=`, `-=`, etc.), and built-in math functions. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | Addition | [`01_addition.py`](./01_addition.py) | Easy | Addition operator `+` |
| 02 | Arithmetic Operations | [`02_arithmetic_operations.py`](./02_arithmetic_operations.py) | Easy ⭐ | `/` float division vs `//` floor division & `%` modulus |
| 03 | Operator Precedence | [`03_operator_precedence.py`](./03_operator_precedence.py) | Easy | Precedence rules (BODMAS/PEMDAS) |
| 04 | Augmented Assignment | [`04_augmented_assignment.py`](./04_augmented_assignment.py) | Easy | `+=`, `-=`, `*=`, `/=` shortcuts |
| 05 | Math Functions | [`05_math_functions.py`](./05_math_functions.py) | Easy | Built-in `abs()`, `pow()`, `round()` |
| 06 | Calculator | [`06_calculator.py`](./06_calculator.py) | Easy | Multi-operation numeric calculation |
| 07 | Discount Calculator | [`07_discount.py`](./07_discount.py) | Easy | Price discount formula evaluation |
| 08 | Profit/Loss | [`08_profit_loss.py`](./08_profit_loss.py) | Easy | Financial profit/loss percentage math |
| 09 | Percentage | [`09_percentage.py`](./09_percentage.py) | Easy | Ratio percentage evaluation |
| 10 | Power Calculator | [`10_power_calculator.py`](./10_power_calculator.py) | Easy | Exponentiation operator `**` |

---

## 📝 Problem Details

### 01. Addition
Add two numbers and print the sum.

```python
a = 15
b = 25
sum_result = a + b

print(f"The sum of {a} and {b} is {sum_result}.")
```

---

### 02. Arithmetic Operations
Demonstrate all fundamental arithmetic operations on two numbers.

```python
a = 17
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Float Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)
```

---

### 03. Operator Precedence
Evaluate expressions combining addition, multiplication, and parentheses to demonstrate order of operations.

```python
result1 = 10 + 5 * 2
result2 = (10 + 5) * 2

print("Without parentheses (10 + 5 * 2):", result1)  # 20
print("With parentheses ((10 + 5) * 2):", result2)     # 30
```

---

### 04. Augmented Assignment
In-place variable modifications using shorthand operators (`+=`, `-=`, `*=`, `/=`).

```python
x = 10
x += 5   # 15
x *= 2   # 30
x -= 4   # 26
x /= 2   # 13.0

print("Final value of x:", x)
```

---

### 05. Math Functions
Utilize built-in mathematical helper functions `abs()`, `pow()`, and `round()`.

```python
num = -15.75
print("Absolute Value:", abs(num))
print("Power (2^5):", pow(2, 5))
print("Rounded:", round(num, 1))
```

---

### 06. Calculator
Compute basic math metrics between two input numbers.

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
```

---

### 07. Discount Calculator
Calculate final selling price after applying a percentage discount to an original price.

```python
original_price = 1200
discount_percent = 15

discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount

print(f"Discount: ${discount_amount}")
print(f"Final Price: ${final_price}")
```

---

### 08. Profit/Loss
Determine profit or loss amount and percentage from Cost Price (CP) and Selling Price (SP).

```python
cost_price = 500
selling_price = 650

profit = selling_price - cost_price
profit_percentage = (profit / cost_price) * 100

print(f"Profit: ${profit} ({profit_percentage}%)")
```

---

### 09. Percentage
Find what percentage a part is of a total.

```python
part = 45
total = 60

percentage = (part / total) * 100
print(f"{part} is {percentage}% of {total}.")
```

---

### 10. Power Calculator
Calculate $base^{exponent}$ using the `**` operator.

```python
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = base ** exponent
print(f"{base}^{exponent} = {result}")
```

---

## ▶️ How to Run

```bash
python 01_addition.py
```

---

## 🎯 Key Takeaways

- `/` **always yields a `float`** in Python 3, even if the division is exact (e.g. `4 / 2 = 2.0`).
- `//` (floor division) truncates the decimal portion toward negative infinity.
- `%` (modulus) extracts the remainder after division.
- Parentheses `()` override default operator precedence.

---

*Author: Karthik Bhandarkar*
