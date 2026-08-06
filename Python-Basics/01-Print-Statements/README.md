# Print Statements & Escape Sequences

Python's built-in `print()` function writes output to the console. Escape sequences
let you embed special characters — newlines, tabs, quotes — directly inside strings.
Together they cover every basic output task you'll encounter in interviews and scripts.

---

## What is it?

`print()` is a built-in function that converts its arguments to strings and writes
them to standard output (the console by default). Escape sequences are backslash
codes (`\n`, `\t`, etc.) that represent characters that can't be typed literally.

---

## Why do we use it?

- Display results, debug values, and format user-facing output.
- Escape sequences let you control layout (newlines, tabs) without extra `print()` calls.
- Comments (`#`, `''' '''`) let you annotate code without affecting execution.

---

## Syntax

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

```python
# Single-line comment
''' Multi-line
    comment '''
```

---

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `*objects` | — | One or more values to print; converted to strings automatically |
| `sep` | `' '` | String inserted between values when multiple are passed |
| `end` | `'\n'` | String appended after the last value |
| `file` | `sys.stdout` | Output stream target |
| `flush` | `False` | Force-flush the stream buffer immediately |

---

## Return Value

`None` — `print()` always returns `None`. It produces a side-effect (output), not a value.

---

## Example

```python
name = "Karthik"
age = 21
print(f"Name: {name}", f"Age: {age}", sep=" | ", end=".\n")
print("Path:\tC:\\Users\\Karthik")   # \t = tab, \\ = literal backslash
print("Line 1\nLine 2\nLine 3")       # \n = newline
```

---

## Output

```
Name: Karthik | Age: 21.
Path:	C:\Users\Karthik
Line 1
Line 2
Line 3
```

---

## Key Points

- `print()` accepts any number of arguments — all are converted to `str` before output.
- `sep` controls what goes **between** values; `end` controls what comes **after** the last one.
- Escape sequences only work inside regular strings, not raw strings (`r"..."`).
- f-strings (`f"..."`) embed expressions directly: `f"{variable}"`.
- `#` comments are ignored by the interpreter; they never appear in output.
- Triple-quoted strings (`'''...'''` or `"""..."""`) span multiple lines and can act as multi-line comments when unassigned.
- `print()` with no arguments outputs a blank line (just `end`, which defaults to `\n`).

---

## Common Mistakes

```python
# Mistake 1 — concatenating non-strings without conversion
age = 21
print("Age: " + age)          # TypeError: can only concatenate str to str
print("Age: " + str(age))     # Correct

# Mistake 2 — forgetting \\ for a literal backslash
print("C:\new_folder")        # \n is a newline — not what you want
print("C:\\new_folder")       # Correct

# Mistake 3 — mismatched quotes
print('He said "hello"')      # OK — outer single, inner double
print("He said "hello"")      # SyntaxError — unescaped inner doubles

# Mistake 4 — sep/end are keyword-only
print("a", "b", ", ")         # Wrong — third arg is treated as a value
print("a", "b", sep=", ")     # Correct
```

---

## Interview Notes

- **When to use:** Any time you need console output — debugging, CLI tools, formatted reports.
- **When NOT to use:** For logging in production code, use the `logging` module instead; it supports levels, file output, and timestamps.
- **Alternative:** `sys.stdout.write()` gives lower-level control (no automatic `\n`, returns character count).
- **f-strings vs `.format()` vs `%`:** f-strings (Python 3.6+) are the modern standard — fastest and most readable. `.format()` is compatible with older codebases. `%` formatting is legacy.
- **Complexity:** O(n) where n = total length of all output — purely I/O bound.

---

## Practice Problems

```
01_hello_world.py
02_print_multiple_lines.py
03_escape_characters.py
04_quotes.py
05_print_shapes.py
06_print_personal_info.py
07_print_formatted_text.py
08_print_special_characters.py
09_print_pattern.py
10_mini_profile.py
```

---

## Quick Revision

```python
# Core syntax
print("Hello")                        # Hello
print("a", "b", sep="-", end="!\n")  # a-b!

# Escape sequences
\n   # newline
\t   # tab
\\   # backslash
\"   # double quote inside string
\'   # single quote inside string

# f-string
name = "Dev"
print(f"Hi {name}")                   # Hi Dev

# Comment styles
# single-line
''' multi
    line '''
```
