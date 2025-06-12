## 🔐 Day 8 Project: Caesar Cipher

### 📄 Table of Contents

- [Overview](#overview)
  - [The Challenge](#the-challenge)
  - [Why This Project Matters](#why-this-project-matters)
  - [Links](#links)
- [My Process](#my-process)
  - [Built With](#built-with)
  - [What I Learned](#what-i-learned)
- [Notes](#notes)

---

## 🔍 Overview

### 🧩 The Challenge

Create a Caesar Cipher program that allows the user to **encode** or **decode** a message by shifting each letter by a chosen number of places in the alphabet. Includes the ability to loop back through the alphabet, handle large shift values, ignore non-letter characters, and repeat the process until the user chooses to stop.

---

### ✅ Why This Project Matters

This project covers all the concepts taught in **Day 8** of Angela Yu’s *100 Days of Code* course. It demonstrates:
- Function parameters and arguments
- String manipulation
- Loops and conditional logic
- Modularization and ASCII art usage
- Reusability and user interaction with loops

This project is sufficient to demonstrate everything taught in Day 8, including exercises and tutorials.

---

### 🔗 Links

- [Solution Code](./day06.py)
- [Original Course](https://www.udemy.com/course/100-days-of-code/)

---

## ⚙️ My Process

### 🧰 Built With

- Python
- `art.py` for ASCII logo
- `input()` for user interaction

---

### 🧠 What I Learned

- How to define and reuse functions with parameters
- How to modify and access elements in a list by index
- How to handle user input loops effectively
- How to validate non-alphabetic characters in strings
- How to work with modulo (`%`) for managing large shift values
- How to maintain user experience using loops and exit conditions

---

## 📝 Notes

- Non-alphabetic characters (e.g., spaces, punctuation) are preserved as-is.
- The shift is normalized using modulo 26 to handle large values.
- Duplicate alphabet list is used to prevent index overflow during character shifts.
- The project includes a replay option and a clear ASCII logo to enhance UX.
