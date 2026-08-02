# 01 - Print Statements

Practice problems covering basic output formatting, escape sequences, quotes, string formatting, and ASCII patterns in Python. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | Hello World | [`01_hello_world.py`](./01_hello_world.py) | Easy | `print()` basics |
| 02 | Print Multiple Lines | [`02_print_multiple_lines.py`](./02_print_multiple_lines.py) | Easy | `\n` escape character |
| 03 | Escape Characters | [`03_escape_characters.py`](./03_escape_characters.py) | Easy | `\t`, `\n`, `\\` escape sequences |
| 04 | Quotes Inside Strings | [`04_quotes.py`](./04_quotes.py) | Easy | Single `'` and Double `"` quote escaping |
| 05 | Print Shapes | [`05_print_shapes.py`](./05_print_shapes.py) | Easy | Multi-line output, right-angled triangle |
| 06 | Print Personal Info | [`06_print_personal_info.py`](./06_print_personal_info.py) | Easy | Sequential `print()` statements |
| 07 | Print Formatted Text | [`07_print_formatted_text.py`](./07_print_formatted_text.py) | Easy | f-strings string formatting |
| 08 | Print Special Characters | [`08_print_special_characters.py`](./08_print_special_characters.py) | Easy | Special characters `@`, `#`, `$`, `%`, `&`, `*` |
| 09 | Print Pattern | [`09_print_pattern.py`](./09_print_pattern.py) | Easy | 5x5 Square grid pattern |
| 10 | Mini Profile Card | [`10_mini_profile.py`](./10_mini_profile.py) | Easy | ASCII text UI layout |

---

## 📝 Problem Details

### 01. Hello World
Print `"Hello, World!"` to the console.

```python
print("Hello, World!")
```

---

### 02. Print Multiple Lines
Print three lines of text using a single `print()` function call.

```python
print("I love Python.\nI am learning to code.\nI will build great projects.")
```

---

### 03. Escape Characters
Demonstrate a tab space (`\t`), new line (`\n`), and backslash (`\\`) in a single statement.

```python
print("Name:\tKarthik\nPath:\tC:\\Users\\Karthik")
```

---

### 04. Quotes Inside Strings
Print a string containing both single and double quotes correctly.

```python
print('He said, "Python\'s syntax is clean."')
```

---

### 05. Print Shapes
Print a right-angled triangle of stars (5 rows) using sequential `print()` calls.

```python
print("*")
print("**")
print("***")
print("****")
print("*****")
```

---

### 06. Print Personal Info
Print personal metadata (Name, Age, City, Hobby) on separate lines.

```python
print("Name: Karthik Bhandarkar")
print("Age: 21")
print("City: Bengaluru")
print("Hobby: Coding")
```

---

### 07. Print Formatted Text
Use f-strings to inject variable values directly into text.

```python
name = "Karthik"
age = 21
print(f"My name is {name} and I am {age} years old.")
```

---

### 08. Print Special Characters
Output special characters `@ # $ % & *` to the console.

```python
print("Special Characters: @ # $ % & *")
```

---

### 09. Print Pattern
Print a 5x5 square pattern made of `#` characters.

```python
print("#####")
print("#####")
print("#####")
print("#####")
print("#####")
```

---

### 10. Mini Profile Card
Design a neat profile card using border characters (`-` and `|`).

```python
print("-----------------------------")
print("| Name : Karthik Bhandarkar |")
print("| Role : Python Learner     |")
print("| Goal : Product-Based Job  |")
print("-----------------------------")
```

---

## ▶️ How to Run

Run any file using Python 3:

```bash
python 01_hello_world.py
```

---

## 🎯 Key Takeaways

- `print()` is the core output function in Python.
- Escape sequences (`\n` for newline, `\t` for tab, `\\` for backslash) enable formatted multiline text within a single string.
- Inverting quote wrappers (e.g. single quotes wrapping double quotes) or using `\'` prevents syntax errors.
- **f-strings** (`f"..."`) allow simple, readable dynamic string interpolation.

---

*Author: Karthik Bhandarkar*
