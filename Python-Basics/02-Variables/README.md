# Variables & Data Types

A variable is a named container that holds a value in memory. Python creates a
variable the moment you assign a value to it — no declaration needed. Every value
has a data type that determines what operations are valid on it.

---

## What is it?

A variable binds a name to an object in memory using the `=` operator. Python is
dynamically typed — the type is determined at runtime by the value assigned, not by
the programmer.

---

## Why do we use it?

- Store and reuse values without hardcoding them repeatedly.
- Give meaningful names to data so code is readable.
- Python's dynamic typing means one variable can hold different types across its lifetime (though this should be done deliberately).

---

## Syntax

```python
variable_name = value          # basic assignment
x = y = z = 0                 # multiple targets, same value
a, b, c = 1, 2.5, "hello"     # tuple unpacking — multiple assignment
a, b = b, a                   # swap without a temp variable
```

---

## Parameters

Variables do not have parameters — they are not functions. The `=` operator is the
assignment operator, not a keyword argument.

| Rule | Detail |
|---|---|
| Starts with | Letter or underscore (`_`) |
| Contains | Letters, digits, underscores |
| Case-sensitive | `name` ≠ `Name` ≠ `NAME` |
| Reserved words | Cannot use Python keywords (`if`, `for`, `class`, etc.) |

---

## Return Value

Assignment (`=`) returns no value — it is a statement, not an expression.
(Exception: walrus operator `:=` does return a value — covered in topic 20.)

---

## Example

```python
name = "Karthik"
age = 21
gpa = 8.7
is_employed = False

# Multiple assignment
x = y = z = 0

# Tuple unpacking
city, country = "Bengaluru", "India"

# Swap
a, b = 10, 20
a, b = b, a

print(name, age, gpa, is_employed)  # Karthik 21 8.7 False
print(x, y, z)                      # 0 0 0
print(city, country)                # Bengaluru India
print(a, b)                         # 20 10
```

---

## Output

```
Karthik 21 8.7 False
0 0 0
Bengaluru India
20 10
```

---

## Key Points

- Python is **dynamically typed** — types are inferred at runtime.
- Use `type()` to inspect a variable's type: `type(42)` → `<class 'int'>`.
- Variable names are **case-sensitive**: `Score` and `score` are two different variables.
- Python naming convention is **snake_case** (`first_name`, not `firstName`).
- A variable can be **reassigned** to a completely different type — Python allows it, but avoid it for readability.
- `del variable_name` removes the binding — accessing it after raises `NameError`.
- Constants by convention use ALL_CAPS (`MAX_SIZE = 100`) — Python has no true constant enforcement.

---

## Common Mistakes

```python
# Mistake 1 — using a reserved keyword as a name
for = 5           # SyntaxError
list = [1, 2, 3]  # Works, but shadows built-in list() — avoid

# Mistake 2 — mixing up = (assignment) and == (comparison)
if x = 10:        # SyntaxError
if x == 10:       # Correct

# Mistake 3 — expecting assignment to return a value
result = (x = 5)  # SyntaxError — use := (walrus) if you need this

# Mistake 4 — unpacking mismatch
a, b = 1, 2, 3    # ValueError: too many values to unpack

# Mistake 5 — assuming global variable is accessible after del
x = 10
del x
print(x)          # NameError: name 'x' is not defined
```

---

## Interview Notes

- **When to use:** Always — variables are fundamental. The key interview question is usually about **scope** (local vs global) or **mutability** of the object being referenced.
- **When NOT to name something a built-in:** Shadowing `list`, `dict`, `input`, `id`, etc. breaks their built-in behavior silently.
- **Alternative for immutability:** Use a tuple or a named constant convention (`ALL_CAPS`) — Python doesn't enforce `const`.
- **Memory note:** Variables in Python are references (pointers) to objects, not boxes containing values. Two variables can point to the same object (`is` checks identity, `==` checks value).
- **Complexity:** O(1) for assignment.

---

## Practice Problems

```
01_store_name.py
02_store_age.py
03_multiple_variables.py
04_swap_variables.py
05_update_variable.py
06_student_information.py
07_employee_details.py
08_calculate_birth_year.py
09_simple_interest.py
10_area_of_rectangle.py
```

---

## Quick Revision

```python
# Assignment
x = 10                     # int
pi = 3.14                  # float
name = "Dev"               # str
active = True              # bool

# Multi-assign
a, b = 1, 2                # tuple unpack
a, b = b, a                # swap

# Type check
type(x)                    # <class 'int'>

# Delete
del x                      # removes binding

# Convention
MAX_LIMIT = 100            # constant (ALL_CAPS)
first_name = "Karthik"     # snake_case
```
