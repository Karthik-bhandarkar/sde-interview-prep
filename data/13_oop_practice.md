# Topic 13: OOP (Object-Oriented Programming) — Practice Set (15 Problems)

---

### Problem 01: Simple Class with One Attribute
**Question:** Create a class `Dog` with a class-level attribute `species = "Canine"`.
Create an object and print the attribute.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Dog:
    species = "Canine"

my_dog = Dog()
print(my_dog.species)
```
**Why classes at all:** A class is a blueprint for creating objects that share
structure — this is the smallest possible example: one blueprint, one shared piece
of data, one object built from it.
</details>

---

### Problem 02: Constructor (__init__)
**Question:** Create a class `Person` with an `__init__` that sets `name` and `age`
for each object individually.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Karthik", 21)
print(p1.name, p1.age)
```
**Why `__init__` and `self`:** `__init__` runs automatically every time you create an
object, setting up its starting data. `self` refers to "this specific object" — it's
how each `Person` object keeps its OWN name and age separate from every other Person object.
</details>

---

### Problem 03: Method Using Instance Attributes
**Question:** Add a method `introduce()` to the `Person` class that prints a sentence
using `self.name` and `self.age`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p1 = Person("Karthik", 21)
p1.introduce()
```
**Why methods need `self` as the first parameter:** When you call `p1.introduce()`,
Python automatically passes `p1` in as `self` — that's how the method knows WHICH
object's name and age to use. Forgetting `self` in a method definition is one of the
most common beginner errors.
</details>

---

### Problem 04: Multiple Objects, Same Class
**Question:** Create three `Person` objects with different data and call `introduce()`
on each.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p1 = Person("Karthik", 21)
p2 = Person("Priya", 23)
p3 = Person("Raj", 25)

for person in (p1, p2, p3):
    person.introduce()
```
**Why one class produces independent objects:** Even though `p1`, `p2`, `p3` all come
from the same `Person` blueprint, each has its own separate `name` and `age` — this
is the whole point of OOP: reuse the structure, keep the data independent.
</details>

---

### Problem 05: Method That Performs a Calculation
**Question:** Create a `BankAccount` class with a `balance` attribute and a
`deposit(amount)` method that adds to the balance.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
```
**Why the method changes `self.balance` directly:** Because `self` refers to this
specific account, `self.balance += amount` permanently updates that object's stored
data — this is different from a plain function, which can't "remember" state between calls.
</details>

---

### Problem 06: Instance Variable vs Class Variable
**Question:** Create a `Car` class with a class variable `wheels = 4` (same for every
car) and an instance variable `brand` (different per car). Demonstrate both.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Car:
    wheels = 4  # class variable — shared by all cars

    def __init__(self, brand):
        self.brand = brand  # instance variable — unique per car

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)
```
**When to use which:** Use a class variable for data that's genuinely the same across
every object (like wheels=4 for a generic Car class). Use an instance variable
(set via `self` in `__init__`) for anything that varies per object.
</details>

---

### Problem 07: Encapsulation Basics
**Question:** Create a `BankAccount` class where `balance` is "private" (prefixed with
`__`), accessible only through a `get_balance()` method.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)
print(account.get_balance())
# print(account.__balance)  # This would raise an AttributeError
```
**Why hide the balance behind a method:** The double-underscore prefix signals "don't
touch this directly from outside the class" — forcing access through `get_balance()`
means you can later add rules (like logging or validation) in ONE place without
changing every place that reads the balance.
</details>

---

### Problem 08: Rectangle Class with area() and perimeter()
**Question:** Create a `Rectangle` class with `length` and `width`, plus methods
`area()` and `perimeter()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
```
**Why bundle data and behavior together:** Before OOP, you'd pass `length` and
`width` into separate functions every time. Here, the Rectangle object carries its
own data AND the operations that make sense on that data — this bundling is the core
idea of OOP.
</details>

---

### Problem 09: Inheritance
**Question:** Create a base class `Animal` with a `speak()` method. Create a `Dog`
class that inherits from `Animal`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    pass

my_dog = Dog()
my_dog.speak()
```
**Why inheritance instead of copy-pasting the method:** `Dog(Animal)` means Dog
automatically gets everything Animal has, without rewriting it. If you later fix a
bug in `Animal.speak()`, every subclass (Dog, Cat, etc.) gets the fix automatically too.
</details>

---

### Problem 10: Method Overriding
**Question:** In the `Dog` class from the previous problem, override `speak()` to
print something dog-specific instead of the generic Animal message.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

Dog().speak()
Cat().speak()
```
**Why overriding matters:** Each subclass keeps the SAME method name (`speak`) but
provides its OWN specific behavior — this means you can treat any Animal-derived
object the same way in your code (`animal.speak()`) and get the right behavior for
whatever type it actually is.
</details>

---

### Problem 11: Using super()
**Question:** Create a `Person` base class with `__init__` setting `name`. Create a
`Student` subclass that adds a `roll_number`, calling the parent's `__init__` using `super()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number

s1 = Student("Karthik", 21)
print(s1.name, s1.roll_number)
```
**Why use super() instead of repeating `self.name = name`:** `super().__init__(name)`
reuses the parent's setup logic instead of duplicating it. If `Person`'s `__init__`
ever gets more complex, `Student` automatically benefits without needing changes.
</details>

---

### Problem 12: Class Method and Static Method
**Question:** Create a `MathHelper` class with a `static method` `square(n)` that
doesn't need any object data, and a `class method` `description()` that returns info
about the class itself.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class MathHelper:
    @staticmethod
    def square(n):
        return n * n

    @classmethod
    def description(cls):
        return f"This is the {cls.__name__} class."

print(MathHelper.square(5))
print(MathHelper.description())
```
**Static vs class vs instance methods:** A regular method needs `self` (a specific
object). A `@staticmethod` needs neither `self` nor `cls` — it's just a utility
function that happens to live inside the class. A `@classmethod` takes `cls` (the
class itself) instead of an object — useful for things that relate to the class as a
whole rather than any one instance.
</details>

---

### Problem 13: Student Class with Percentage Calculation
**Question:** Create a `Student` class storing marks in 5 subjects (as a list), with a
method `calculate_percentage()`.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of 5 subject marks

    def calculate_percentage(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Karthik", [88, 92, 76, 85, 90])
print(f"{s1.name}'s percentage: {s1.calculate_percentage()}%")
```
**Why store marks as a list inside the object:** This combines earlier topics —
lists (Topic 09) stored as an instance attribute, with a method that processes them.
Real OOP code constantly reuses lists, dicts, loops, and conditionals inside class methods.
</details>

---

### Problem 14: Simple Stack Using a Class
**Question:** Create a `Stack` class using a list internally, with `push(item)`,
`pop()`, and `is_empty()` methods.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())
```
**Why wrap a list in a class instead of using it directly:** The `Stack` class
restricts HOW the list can be used (only push/pop from one end) and hides the raw
list from outside code — this is the first real taste of building a "data structure,"
which is exactly what DSA practice (your next step after this) is built on.
</details>

---

### Problem 15: Car Class Modeling a Real Object
**Question:** Create a `Car` class with `brand`, `model`, and `year` attributes, and a
`display_info()` method that prints all three in a readable sentence.

```python
# ✍️ Your attempt

```

<details>
<summary>✅ Solution + Why</summary>

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2023)
car2 = Car("Honda", "Civic", 2022)

car1.display_info()
car2.display_info()
```
**Why this is the natural "final" OOP problem here:** It combines everything from
this topic — constructor, instance attributes, and a method — to model something
concrete from the real world. This "model a real-world thing as a class" pattern is
what you'll use for almost every OOP problem going forward.
</details>
