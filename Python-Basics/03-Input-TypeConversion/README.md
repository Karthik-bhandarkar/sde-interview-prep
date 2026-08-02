# 03 - Input & Type Conversion

Practice problems covering user input handling with `input()`, type casting (`int()`, `float()`), arithmetic with dynamic user data, and output precision using `round()`. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | Name Input | [`01_name_input.py`](./01_name_input.py) | Easy | `input()` returning string |
| 02 | Age Input | [`02_age_input.py`](./02_age_input.py) | Easy | `int(input())` type conversion |
| 03 | Birth Year | [`03_birth_year.py`](./03_birth_year.py) | Easy | Subtracting converted `int` input |
| 04 | BMI Input | [`04_bmi_input.py`](./04_bmi_input.py) | Easy ⭐ | `float(input())`, BMI formula $w / h^2$ |
| 05 | Temperature Converter | [`05_temperature_converter.py`](./05_temperature_converter.py) | Easy | Celsius to Fahrenheit conversion |
| 06 | Add Two Numbers | [`06_add_two_numbers.py`](./06_add_two_numbers.py) | Easy | Numeric casting vs string concatenation |
| 07 | Area of Circle | [`07_area_circle.py`](./07_area_circle.py) | Easy | Formula evaluation $\pi r^2$ with `round()` |
| 08 | Simple Interest | [`08_simple_interest.py`](./08_simple_interest.py) | Easy | Multi-input type casting & calculation |
| 09 | Currency Converter | [`09_currency_converter.py`](./09_currency_converter.py) | Easy | Exchange rate arithmetic |
| 10 | Percentage Calculator | [`10_percentage_calculator.py`](./10_percentage_calculator.py) | Easy | Marks percentage computation |

---

## 📝 Problem Details

### 01. Name Input
Read the user's name and greet them.

```python
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python.")
```

---

### 02. Age Input
Read user age, convert it to an integer, and print next year's age.

```python
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1} years old.")
```

---

### 03. Birth Year
Compute birth year dynamically based on user age input.

```python
age = int(input("Enter your age: "))
current_year = 2026
birth_year = current_year - age

print(f"Your birth year is approximately {birth_year}.")
```

---

### 04. BMI Input
Calculate Body Mass Index from weight (kg) and height (m) user inputs.

```python
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is {round(bmi, 2)}.")
```

---

### 05. Temperature Converter
Convert Celsius input to Fahrenheit ($F = C \times \frac{9}{5} + 32$).

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F.")
```

---

### 06. Add Two Numbers
Prompt for two numbers, cast to integer, and display their sum.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}.")
```

---

### 07. Area of Circle
Calculate circle area ($\pi \times r^2$) from user radius input.

```python
radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
area = pi * (radius ** 2)

print(f"The area of the circle is {round(area, 2)}.")
```

---

### 08. Simple Interest
Prompt for Principal, Rate, and Time to calculate simple interest dynamically.

```python
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time in years: "))

si = (p * r * t) / 100
print(f"Simple Interest: {si}")
```

---

### 09. Currency Converter
Convert USD input to INR based on a fixed conversion rate.

```python
usd = float(input("Enter amount in USD: "))
exchange_rate = 83.5
inr = usd * exchange_rate

print(f"${usd} USD is equivalent to ₹{round(inr, 2)} INR.")
```

---

### 10. Percentage Calculator
Calculate score percentage based on obtained marks and total marks.

```python
obtained = float(input("Enter obtained marks: "))
total = float(input("Enter total marks: "))

percentage = (obtained / total) * 100
print(f"Percentage: {round(percentage, 2)}%")
```

---

## ▶️ How to Run

```bash
python 01_name_input.py
```

---

## 🎯 Key Takeaways

- `input()` **always returns a string**. Explicit casting (`int()`, `float()`) is required for numeric computations.
- Attempting math on raw `input()` leads to string repetition (`"5" + "5" = "55"`) rather than addition (`5 + 5 = 10`).
- `round(value, decimals)` limits float output precision to clean up UI display.

---

*Author: Karthik Bhandarkar*
