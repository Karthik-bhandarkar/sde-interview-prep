# If-Else (Conditional Statements)

Conditional statements let a program choose which block of code to run based on
whether a condition is `True` or `False`. Python uses `if`, `elif`, and `else` for
branching, and supports ternary expressions for simple one-line decisions.

---

## What is it?

An `if` statement evaluates a Boolean expression. If it is truthy, the indented
block runs. `elif` (else-if) adds additional conditions. `else` is a catch-all that
runs when no previous condition matched. All branches are mutually exclusive —
only the first matching block executes.

---

## Why do we use it?

- Control which code path runs depending on runtime data (user input, API response, computed value).
- Guard against edge cases (e.g., division by zero, invalid input).
- Replace repetitive boolean logic with a readable decision tree.

---

## Syntax

```python
# Basic if-elif-else
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
else:
    # runs if all conditions above are False

# Ternary (one-liner)
value = "even" if n % 2 == 0 else "odd"

# Nested if
if outer_condition:
    if inner_condition:
        # runs only when both are True
```

---

## Parameters

`if` / `elif` accept any expression that evaluates to a truthy or falsy value:

| Falsy values | Truthy values |
|---|---|
| `False`, `0`, `0.0` | `True`, any non-zero number |
| `""`, `[]`, `{}`, `()`, `set()` | Any non-empty string, list, dict, etc. |
| `None` | Any object not listed as falsy |

---

## Return Value

`if`/`elif`/`else` are **statements**, not expressions — they produce no value.
The **ternary expression** (`x if condition else y`) does return a value.

---

## Example

```python
age = 20

if age < 18:
    print("Minor")
elif age == 18:
    print("Just became an adult")
else:
    print("Adult")

# Ternary
label = "even" if age % 2 == 0 else "odd"
print(f"{age} is {label}")
```

---

## Output

```
Adult
20 is even
```

---

## Key Points

- Python uses **indentation** (4 spaces) to define blocks — there are no braces.
- `elif` is optional and can be chained as many times as needed.
- `else` is optional — an `if` with no `else` simply does nothing when the condition is `False`.
- Conditions can use any combination of comparison, logical, membership, and identity operators.
- **Ternary syntax:** `x if condition else y` — useful for simple assignments, not for complex logic.
- **Truthiness:** Non-empty containers, non-zero numbers, and non-`None` values are truthy.
- Python evaluates `and`/`or` with short-circuiting — useful for guard patterns: `if x and x > 0`.

---

## Common Mistakes

```python
# Mistake 1 — using = instead of == in condition
if x = 10:             # SyntaxError
if x == 10:            # Correct

# Mistake 2 — missing colon
if x > 5               # SyntaxError: expected ':'
if x > 5:              # Correct

# Mistake 3 — incorrect indentation
if x > 5:
print("yes")           # IndentationError
    print("yes")       # Correct

# Mistake 4 — using elif after else
if x > 5:
    pass
else:
    pass
elif x == 5:           # SyntaxError — elif must come before else
    pass

# Mistake 5 — comparing to True/False explicitly (redundant)
if is_valid == True:   # redundant
if is_valid:           # Pythonic
```

---

## Interview Notes

- **When to use:** Any time execution depends on a condition — validation, routing, state machines.
- **When NOT to nest deeply:** More than 2–3 levels of nesting is a sign to refactor — extract functions or use guard clauses (early return).
- **Alternative — dictionary dispatch:** Replace long `if/elif` chains on a fixed set of keys with a dictionary:
  ```python
  actions = {"start": start_fn, "stop": stop_fn}
  actions.get(command, default_fn)()
  ```
- **Alternative — match-case (Python 3.10+):** Cleaner than `if/elif` for matching against multiple literal values.
- **Complexity:** O(1) per condition evaluation (each comparison runs in constant time).

---

## Practice Problems

```
01_if_else.py
02_even_or_odd.py
03_voting_eligibility.py
04_largest_of_two.py
05_largest_of_three.py
06_driving_license_checker.py
07_bank_account_access.py
08_hackerrank_python_if_else.py
09_gfg_if_conditional_statement.py
```

---

## Quick Revision

```python
# if / elif / else
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Ternary
result = "yes" if x > 0 else "no"

# Falsy check
if not value:           # covers None, 0, "", [], {}
    print("empty")

# Guard clause pattern
if not condition:
    return              # exit early, keep nesting shallow
# main logic here
```