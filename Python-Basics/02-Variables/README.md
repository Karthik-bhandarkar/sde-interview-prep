# 02 - Variables

Practice problems covering variable initialization, dynamic typing, variable swapping, value updates, and practical mathematical applications. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | Store Name | [`01_store_name.py`](./01_store_name.py) | Easy | String variable assignment |
| 02 | Store Age | [`02_store_age.py`](./02_store_age.py) | Easy | Integer variable assignment |
| 03 | Multiple Variables | [`03_multiple_variables.py`](./03_multiple_variables.py) | Easy | Multiple assignment on one line |
| 04 | Swap Variables | [`04_swap_variables.py`](./04_swap_variables.py) | Easy ⭐ | Tuple unpacking `a, b = b, a` |
| 05 | Update Variable | [`05_update_variable.py`](./05_update_variable.py) | Easy | Re-assigning variable values |
| 06 | Student Information | [`06_student_information.py`](./06_student_information.py) | Easy | Mixed data types (str, int, float, bool) |
| 07 | Employee Details | [`07_employee_details.py`](./07_employee_details.py) | Easy | Variable composition & output formatting |
| 08 | Calculate Birth Year | [`08_calculate_birth_year.py`](./08_calculate_birth_year.py) | Easy | Arithmetic with variables |
| 09 | Simple Interest | [`09_simple_interest.py`](./09_simple_interest.py) | Easy | Formula evaluation `(P * R * T) / 100` |
| 10 | Area of Rectangle | [`10_area_of_rectangle.py`](./10_area_of_rectangle.py) | Easy | Formula evaluation `length * width` |

---

## 📝 Problem Details

### 01. Store Name
Store a string in a variable and display it.

```python
name = "Karthik Bhandarkar"
print("Name:", name)
```

---

### 02. Store Age
Store an integer representing age and print it.

```python
age = 21
print("Age:", age)
```

---

### 03. Multiple Variables
Declare and assign multiple variables in a single line.

```python
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)
```

---

### 04. Swap Variables
Swap two variables without using a temporary variable using Python's tuple unpacking.

```python
a = 5
b = 10
print("Before swap -> a:", a, ", b:", b)

a, b = b, a
print("After swap  -> a:", a, ", b:", b)
```

---

### 05. Update Variable
Demonstrate variable mutability by modifying its value during execution.

```python
score = 0
print("Initial Score:", score)

score = 100
print("Updated Score:", score)
```

---

### 06. Student Information
Store name, age, GPA, and enrollment status using appropriate data types.

```python
name = "Karthik"
age = 21
gpa = 3.8
is_enrolled = True

print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Enrolled:", is_enrolled)
```

---

### 07. Employee Details
Store employee ID, designation, and salary, printing a formatted summary.

```python
emp_id = 101
designation = "Software Engineer"
salary = 75000.50

print(f"Employee #{emp_id}: {designation} earning ${salary}")
```

---

### 08. Calculate Birth Year
Compute birth year using current year and age variables.

```python
current_year = 2026
age = 21
birth_year = current_year - age

print("Birth Year:", birth_year)
```

---

### 09. Simple Interest
Calculate simple interest given Principal, Rate, and Time.

```python
principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)
```

---

### 10. Area of Rectangle
Calculate area from length and width variables.

```python
length = 15
width = 8

area = length * width
print("Area of Rectangle:", area)
```

---

## ▶️ How to Run

```bash
python 01_store_name.py
```

---

## 🎯 Key Takeaways

- Variables act as named containers for storing data values.
- Python is **dynamically typed**, so type annotations are optional and variable types can change at runtime.
- Python allows simultaneous assignment (e.g. `x, y, z = 1, 2, 3`).
- **Tuple Unpacking** (`a, b = b, a`) provides an elegant $O(1)$ swap without temporary storage.

---

*Author: Karthik Bhandarkar*
