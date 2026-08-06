# Input & Type Conversion

`input()` pauses execution and reads a line typed by the user, returning it as a
string. Type conversion (typecasting) transforms a value from one data type to
another using built-in functions like `int()`, `float()`, `str()`, and `bool()`.

---

## What is it?

- **`input()`** — a built-in function that reads a line from standard input (keyboard) and returns it as a `str`.
- **Typecasting** — explicitly converting a value's type using `int()`, `float()`, `str()`, or `bool()`.

Python always returns `input()` as a string. Any numerical computation requires an explicit conversion first.

---

## Why do we use it?

- Accept dynamic values from a user at runtime instead of hardcoding data.
- Convert between types so operations work correctly (e.g., adding numbers read from input requires `int()` or `float()` conversion).
- Control data flow by coercing types to a predictable format.

---

## Syntax

```python
variable = input("Prompt message: ")       # always returns str

# Typecasting
int_val   = int("42")                      # str → int
float_val = float("3.14")                  # str → float
str_val   = str(100)                       # int → str
bool_val  = bool(0)                        # 0 → False, non-zero → True
```

---

## Parameters

### `input(prompt="")`

| Parameter | Default | Description |
|---|---|---|
| `prompt` | `""` | String printed to stdout before waiting for input |

### Conversion functions

| Function | Converts to | Notes |
|---|---|---|
| `int(x)` | Integer | Truncates floats; raises `ValueError` on non-numeric strings |
| `float(x)` | Float | Accepts integers and numeric strings |
| `str(x)` | String | Works on any type |
| `bool(x)` | Boolean | `0`, `""`, `[]`, `None` → `False`; everything else → `True` |

---

## Return Value

| Function | Returns |
|---|---|
| `input()` | `str` — always |
| `int()` | `int` |
| `float()` | `float` |
| `str()` | `str` |
| `bool()` | `bool` |

---

## Example

```python
name = input("Enter your name: ")            # "Karthik"
age  = int(input("Enter your age: "))        # "21" → 21
gpa  = float(input("Enter your GPA: "))      # "8.7" → 8.7

print(f"Hello {name}, age {age}, GPA {gpa}")
print(type(name), type(age), type(gpa))
```

---

## Output

```
Enter your name: Karthik
Enter your age: 21
Enter your GPA: 8.7
Hello Karthik, age 21, GPA 8.7
<class 'str'> <class 'int'> <class 'float'>
```

---

## Key Points

- `input()` **always** returns a `str` — forgetting this is the #1 beginner mistake.
- `int("3.14")` raises `ValueError` — convert floats with `float()` first, then `int()`.
- `int()` on a float **truncates** (does not round): `int(3.9)` → `3`.
- `bool()` of any non-zero number, non-empty string, or non-empty collection is `True`.
- `str()` works on every Python object — it calls the object's `__str__` method.
- Chaining conversions inline is clean: `int(input("Age: "))`.
- `input()` blocks execution until the user presses Enter.

---

## Common Mistakes

```python
# Mistake 1 — adding numbers without converting input
a = input("Num 1: ")
b = input("Num 2: ")
print(a + b)             # "35" (string concat) — NOT 8

print(int(a) + int(b))   # Correct: 8

# Mistake 2 — converting a float-string to int directly
val = "3.14"
int(val)                 # ValueError: invalid literal for int()
int(float(val))          # Correct: 3

# Mistake 3 — assuming input() returns a number
x = input("Enter number: ")
print(x * 2)             # "55" not 10 — it repeats the string

# Mistake 4 — bool("False") is True
bool("False")            # True — non-empty string is always True
bool("")                 # False
```

---

## Interview Notes

- **When to use `input()`:** CLI scripts, interactive programs, coding challenges that require runtime input (e.g., competitive programming).
- **When NOT to use:** In production APIs or web backends — use request parameters or config files instead.
- **Alternative:** `sys.stdin.readline()` for performance in competitive programming (faster than `input()` for large inputs).
- **Validation pattern:** Always wrap `input()` conversion in `try/except ValueError` for robust CLI tools.
- **Complexity:** O(n) where n = length of the input string.

---

## Practice Problems

```
01_name_input.py
02_age_input.py
03_birth_year.py
04_bmi_input.py
05_temperature_converter.py
06_add_two_numbers.py
07_area_circle.py
08_simple_interest.py
09_currency_converter.py
10_percentage_calculator.py
```

---

## Quick Revision

```python
# Reading input (always str)
name = input("Name: ")

# Inline conversion
age  = int(input("Age: "))
gpa  = float(input("GPA: "))

# Manual conversion
int("42")          # 42
float("3.14")      # 3.14
str(100)           # "100"
bool(0)            # False
bool("hi")         # True

# Safe conversion
try:
    val = int(input("Enter int: "))
except ValueError:
    print("Not a valid integer")
```
