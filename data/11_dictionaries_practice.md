# Topic 11: Dictionaries — Practice Set (12 Problems)

---

### Problem 01: Create and Print a Dictionary
**Question:** Create a dictionary storing a person's name, age, and city, then print it.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = {"name": "Karthik", "age": 21, "city": "Bengaluru"}
print(person)
```
**Why a dictionary over a tuple here:** A tuple `("Karthik", 21, "Bengaluru")` forces
you to remember that index 0 is name, index 1 is age. A dictionary labels each value
with a key — use a dict whenever the data has named fields, not just an ordered sequence.
</details>

---

### Problem 02: Access Values with Keys and get()
**Question:** From a dictionary, access a value using square brackets AND using
`.get()`, including a key that doesn't exist.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = {"name": "Karthik", "age": 21}
print(person["name"])
print(person.get("age"))
print(person.get("country", "Not specified"))
```
**Why `.get()` is safer:** `person["country"]` would crash with a `KeyError` since
that key doesn't exist. `.get("country", "Not specified")` returns a default value
instead of crashing — use `.get()` whenever a key might legitimately be missing.
</details>

---

### Problem 03: Add and Update Key-Value Pairs
**Question:** Add a new key to a dictionary, and update the value of an existing key.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = {"name": "Karthik", "age": 21}
person["city"] = "Bengaluru"
person["age"] = 22
print(person)
```
**Why the same syntax does both:** `dict[key] = value` adds the key if it doesn't
exist, or overwrites it if it does — Python doesn't need a separate "update" syntax
because the operation is identical either way.
</details>

---

### Problem 04: Delete Keys
**Question:** Delete one key using `del` and another using `.pop()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = {"name": "Karthik", "age": 21, "city": "Bengaluru"}
del person["city"]
removed_value = person.pop("age")
print(person)
print("Removed value was:", removed_value)
```
**del vs pop():** `del` just deletes, giving nothing back. `.pop(key)` deletes AND
returns the value that was removed — use `.pop()` when you still need that value
afterward, `del` when you don't.
</details>

---

### Problem 05: Loop Through Keys, Values, Items
**Question:** Given a dictionary, loop through and print just the keys, then just the
values, then both together.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = {"name": "Karthik", "age": 21, "city": "Bengaluru"}

print("Keys:")
for key in person.keys():
    print(key)

print("Values:")
for value in person.values():
    print(value)

print("Items:")
for key, value in person.items():
    print(key, ":", value)
```
**Why three different methods:** `.keys()`, `.values()`, and `.items()` exist
because different tasks need different views of the same data — looping with
`.items()` (both at once) is what you'll use most often in real code.
</details>

---

### Problem 06: Check if a Key Exists
**Question:** Check whether a specific key exists in a dictionary before accessing it.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = {"name": "Karthik", "age": 21}
if "city" in person:
    print(person["city"])
else:
    print("City not found in dictionary")
```
**Why check `in` the dictionary itself:** `"city" in person` checks the KEYS by
default (not the values) — this is the safe way to avoid a `KeyError` when you're not
sure a key exists, as an alternative to `.get()`.
</details>

---

### Problem 07: Length of a Dictionary
**Question:** Find how many key-value pairs a dictionary has.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
person = {"name": "Karthik", "age": 21, "city": "Bengaluru"}
print("Number of entries:", len(person))
```
**Why len() works the same as lists:** `len()` is a general-purpose "how many items"
function across strings, lists, tuples, AND dictionaries — for a dict, it counts
key-value pairs, not individual keys or values separately.
</details>

---

### Problem 08: Merge Two Dictionaries
**Question:** Merge two dictionaries into one using `.update()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
dict1 = {"name": "Karthik", "age": 21}
dict2 = {"city": "Bengaluru", "age": 22}
dict1.update(dict2)
print(dict1)
```
**What happens with overlapping keys:** Notice `age` exists in both — after
`.update()`, dict1's `age` becomes 22 (dict2's value wins). Whoever calls `.update()`
LAST for a given key overwrites the earlier value.
</details>

---

### Problem 09: Build a Dictionary from Two Lists
**Question:** Given a list of names and a list of marks, combine them into a dictionary
using `zip()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
names = ["Karthik", "Raj", "Priya"]
marks = [88, 76, 92]
student_marks = dict(zip(names, marks))
print(student_marks)
```
**Why zip() over a manual loop:** `zip()` pairs up elements from two lists by
position in one step; the manual alternative (`for i in range(len(names)):
student_marks[names[i]] = marks[i]`) works but is longer and more error-prone.
</details>

---

### Problem 10: Character Frequency Counter
**Question:** Given a string, count how many times each character appears using a dictionary.

**Think about it:**
- For each character, check if it's already a key. If yes, increase its count; if no,
  add it with count 1. (Or look up `.get()` with a default of 0.)

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
text = "banana"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)
```
**Why `.get(char, 0)` is the key trick:** On the first occurrence of a character,
`frequency.get(char, 0)` safely returns 0 (since it's not a key yet) instead of
crashing — this "count with a dictionary" pattern is one of the most reused patterns
in real interview problems (anagrams, duplicates, majority element, etc).
</details>

---

### Problem 11: Nested Dictionary — Student Records
**Question:** Store multiple students' records (each with age and marks) in a nested
dictionary, then print one student's details.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
students = {
    "Karthik": {"age": 21, "marks": 88},
    "Priya": {"age": 22, "marks": 92}
}
print(students["Karthik"])
print("Karthik's marks:", students["Karthik"]["marks"])
```
**Why nesting instead of one flat dictionary:** A flat dict can't cleanly represent
"a collection of records, each with multiple fields" — nesting a dict inside a dict
mirrors how real-world data (like JSON from an API) is actually structured.
</details>

---

### Problem 12: Key with Maximum Value
**Question:** Given a dictionary of students and their marks, find the student with
the highest marks.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
marks = {"Karthik": 88, "Raj": 76, "Priya": 92, "Anu": 85}
top_student = max(marks, key=marks.get)
print("Top student:", top_student, "with", marks[top_student], "marks")
```
**Why `key=marks.get`:** By default, `max()` on a dictionary compares the KEYS
(alphabetically), not the values. Passing `key=marks.get` tells `max()` to compare
each key by looking up its VALUE instead — this `key=` pattern is used constantly for
custom sorting/comparison logic in Python.
</details>
