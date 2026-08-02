# 04 - Strings

Practice problems covering string initialization, indexing, slicing, f-strings, and string manipulation methods in Python. Part of the [SDE Interview Prep](https://github.com/Karthik-bhandarkar/sde-interview-prep) series under `Python-Basics`.

## 📋 Problems

| # | Problem | File | Difficulty | Concepts |
|---|---------|------|------------|----------|
| 01 | String Basics | [`01_string_basics.py`](./01_string_basics.py) | Easy | String creation & `len()` |
| 02 | String Indexing | [`02_string_indexing.py`](./02_string_indexing.py) | Easy | Positive & negative indexing `s[0]`, `s[-1]` |
| 03 | String Slicing | [`03_string_slicing.py`](./03_string_slicing.py) | Easy ⭐ | Substrings `s[start:stop:step]` |
| 04 | Formatted Strings | [`04_formatted_strings.py`](./04_formatted_strings.py) | Easy | Dynamic interpolation with `f"..."` |
| 05 | String Methods | [`05_string_methods.py`](./05_string_methods.py) | Easy | `.upper()`, `.lower()`, `.strip()` |
| 06 | Full Name | [`06_full_name.py`](./06_full_name.py) | Easy | Concatenation & string joining |
| 07 | Reverse Name | [`07_reverse_name.py`](./07_reverse_name.py) | Easy ⭐ | Reverse slicing `s[::-1]` |
| 08 | Count Characters | [`08_count_characters.py`](./08_count_characters.py) | Easy | Character counting with `.count()` / `len()` |
| 09 | Find Character | [`09_find_character.py`](./09_find_character.py) | Easy | Substring search with `.find()` |
| 10 | Replace Word | [`10_replace_word.py`](./10_replace_word.py) | Easy | Substring replacement with `.replace()` |

---

## 📝 Problem Details

### 01. String Basics
Store a string and print its value along with its total character count using `len()`.

```python
text = "Python Programming"
print("Text:", text)
print("Length:", len(text))
```

---

### 02. String Indexing
Access first, last, and specific index characters using positive and negative indexing.

```python
s = "Developer"
print("First character:", s[0])
print("Last character:", s[-1])
print("Third character:", s[2])
```

---

### 03. String Slicing
Extract substrings using slicing notation `[start:stop:step]`.

```python
s = "HelloWorld"
print("First 5 chars:", s[0:5])
print("Chars from index 5:", s[5:])
print("Every second char:", s[::2])
```

---

### 04. Formatted Strings
Inject variables seamlessly using f-string syntax.

```python
language = "Python"
version = 3.12
print(f"I am coding in {language} version {version}.")
```

---

### 05. String Methods
Demonstrate common built-in string methods `.upper()`, `.lower()`, and `.strip()`.

```python
raw_text = "  python code  "
print("Upper:", raw_text.upper())
print("Lower:", raw_text.lower())
print("Stripped:", raw_text.strip())
```

---

### 06. Full Name
Combine first name and last name into a full name using string concatenation and f-strings.

```python
first_name = "Karthik"
last_name = "Bhandarkar"
full_name = f"{first_name} {last_name}"

print("Full Name:", full_name)
```

---

### 07. Reverse Name
Reverse a string using step slicing `[::-1]`.

```python
name = "Karthik"
reversed_name = name[::-1]

print("Reversed:", reversed_name)
```

---

### 08. Count Characters
Count occurrences of a specific character within a string.

```python
sentence = "python programming language"
char_count = sentence.count("g")

print("Occurrences of 'g':", char_count)
```

---

### 09. Find Character
Locate the index position of a substring using `.find()`.

```python
text = "Learn Python Programming"
index = text.find("Python")

print("Index of 'Python':", index)
```

---

### 10. Replace Word
Replace words in a string using `.replace()`.

```python
sentence = "Java is easy and fun."
updated_sentence = sentence.replace("Java", "Python")

print("Updated:", updated_sentence)
```

---

## ▶️ How to Run

```bash
python 01_string_basics.py
```

---

## 🎯 Key Takeaways

- Strings in Python are **immutable** — string methods return new modified strings without mutating the original.
- **Indexing** starts at `0` for forward indexing and `-1` for reverse indexing.
- **Slicing** syntax `s[start:stop:step]` enables instant extraction and string reversal (`s[::-1]`).
- Methods like `.strip()`, `.upper()`, `.find()`, and `.replace()` provide fast text manipulation.

---

*Author: Karthik Bhandarkar*
