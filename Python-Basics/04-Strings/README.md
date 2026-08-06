# Strings (Basics)

A string is an ordered, immutable sequence of characters. Python treats strings as
a first-class type with rich built-in methods for searching, slicing, formatting,
and transformation — all without modifying the original string.

---

## What is it?

A `str` object is an immutable sequence of Unicode characters. Strings can be
created with single quotes, double quotes, or triple quotes, and support indexing,
slicing, and a large set of built-in methods.

---

## Why do we use it?

- Store and manipulate any text data — names, messages, file paths, JSON keys.
- Python's string methods cover most text-processing needs without external libraries.
- Immutability makes strings safe to share across functions without defensive copying.

---

## Syntax

```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = """triple quotes
        span multiple lines"""

# Indexing
s[0]      # first character
s[-1]     # last character

# Slicing
s[start:stop:step]
s[:5]     # first 5 chars
s[7:]     # from index 7 to end
s[::-1]   # reversed
```

---

## Parameters

String methods are called on the string object itself. Key methods:

| Method | Description |
|---|---|
| `.upper()` / `.lower()` | Change case |
| `.strip()` / `.lstrip()` / `.rstrip()` | Remove whitespace |
| `.replace(old, new)` | Substitute substring |
| `.split(sep)` | Split into list by separator |
| `.join(iterable)` | Join list items into a string |
| `.find(sub)` | Return index of first match, or `-1` |
| `.count(sub)` | Count non-overlapping occurrences |
| `.startswith(s)` / `.endswith(s)` | Return `bool` |
| `.isdigit()` / `.isalpha()` / `.isalnum()` | Check character class |
| `len(s)` | Length (built-in function, not a method) |

---

## Return Value

All string methods return **new strings** — the original is never modified (strings are immutable).

---

## Example

```python
text = "  Hello, Python!  "

print(text.strip())                    # "Hello, Python!"
print(text.upper())                    # "  HELLO, PYTHON!  "
print(text.replace("Python", "World")) # "  Hello, World!  "

words = "apple,banana,orange"
fruits = words.split(",")              # ['apple', 'banana', 'orange']
print(" - ".join(fruits))             # "apple - banana - orange"

name = "Karthik"
print(f"Hello, {name}!")              # "Hello, Karthik!"
print(name[0])                        # "K"
print(name[-1])                       # "k"
print(name[::-1])                     # "kihtraK"
```

---

## Output

```
Hello, Python!
  HELLO, PYTHON!  
  Hello, World!  
apple - banana - orange
Hello, Karthik!
K
k
kihtraK
```

---

## Key Points

- Strings are **immutable** — every method returns a new string, never modifies in place.
- Indexing starts at `0`; negative indices count from the end (`-1` = last char).
- Slicing `s[start:stop:step]` — `stop` is exclusive.
- `len(s)` is O(1) — Python caches the length.
- `''.join(list)` is faster than concatenating with `+` in a loop.
- f-strings (Python 3.6+) support expressions: `f"{x * 2:.2f}"`.
- `str` supports `in` for membership: `"py" in "python"` → `True`.

---

## Common Mistakes

```python
# Mistake 1 — trying to mutate a string
s = "hello"
s[0] = "H"             # TypeError: 'str' object does not support item assignment
s = "H" + s[1:]        # Correct: build a new string

# Mistake 2 — off-by-one in slicing
s = "Python"
print(s[0:3])           # "Pyt" — stop index is exclusive

# Mistake 3 — using find() and not checking -1
s = "hello"
idx = s.find("z")       # -1 (not found)
print(s[idx])           # "o" — accidentally uses s[-1], no error!
if idx != -1:
    print(s[idx])       # Safe

# Mistake 4 — concatenation in a loop
result = ""
for word in ["a", "b", "c"]:
    result += word      # O(n²) — creates a new string each iteration
result = "".join(["a", "b", "c"])  # O(n) — correct

# Mistake 5 — split() vs split(" ")
"  a  b  ".split()      # ['a', 'b'] — strips and splits on any whitespace
"  a  b  ".split(" ")   # ['', '', 'a', '', 'b', '', ''] — literal space split
```

---

## Interview Notes

- **When to use:** Anytime text data is involved — parsing, formatting, validation.
- **When NOT to use `+` for concatenation in loops:** Use `''.join()` — O(n) vs O(n²).
- **Immutability trade-off:** Strings are thread-safe but create new objects on every "modification".
- **`in` operator:** O(n) substring check — for performance-critical search, consider `str.find()` or regex.
- **Complexity:**
  - Indexing: O(1)
  - Slicing: O(k) where k = slice length
  - `len()`: O(1)
  - `.find()`, `.replace()`, `.split()`: O(n)

---

## Practice Problems

```
01_string_basics.py
02_string_indexing.py
03_string_slicing.py
04_formatted_strings.py
05_string_methods.py
06_full_name.py
07_reverse_name.py
08_count_characters.py
09_find_character.py
10_replace_word.py
```

---

## Quick Revision

```python
s = "Hello, Python!"

# Indexing & Slicing
s[0]          # 'H'
s[-1]         # '!'
s[0:5]        # 'Hello'
s[::-1]       # '!nohtyP ,olleH'

# Methods
s.upper()                  # 'HELLO, PYTHON!'
s.lower()                  # 'hello, python!'
s.strip()                  # (removes leading/trailing whitespace)
s.replace("Hello", "Hi")  # 'Hi, Python!'
s.split(", ")              # ['Hello', 'Python!']
", ".join(["a", "b"])      # 'a, b'
s.find("Python")           # 7
len(s)                     # 14

# f-string
name = "Dev"
f"Hi {name}!"              # 'Hi Dev!'
```
