# 🐾 Assignment: Animals with Polymorphism

## 🧠 Objective

Demonstrate the use of **polymorphism** in Python by creating an `Animal` base class and several subclasses, each implementing a unique version of the `move()` method.

---

## 🐍 Code Structure

### `Animal` (Base Class)

Defines a general `move()` method, intended to be overridden.

### Subclasses:

| Class     | move() Output     |
|-----------|-------------------|
| `Dog`     | "Running 🐕"       |
| `Bird`    | "Flying 🐦"        |
| `Fish`    | "Swimming 🐟"      |
| `Snake`   | "Slithering 🐍"    |
| `Kangaroo`| "Hopping 🦘"       |

Each subclass inherits from `Animal` and provides a specific implementation of `move()`.

---

## 📦 Features Demonstrated

| Feature         | Description                                  |
|-----------------|----------------------------------------------|
| Polymorphism    | All classes implement `move()` differently   |
| Inheritance     | All animals inherit from the `Animal` class  |
| Method Overriding | Each subclass overrides `move()`           |
| Encapsulation   | Logic is contained within each class         |

---

## ▶️ How to Run

1. Clone or download the repo
2. Run the script:

```bash
python animals.py
