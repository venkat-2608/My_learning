## 🎯 Day 7 Project: Beginner Hangman

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

Build a classic **Hangman** game using Python, which selects a random word, displays blanks, accepts letter guesses, and reveals correct guesses or reduces lives on incorrect attempts. Includes ASCII art to represent the stages of the hangman.

---

### ✅ Why This Project Matters

This project covers all the topics taught in **Day 7** of Angela Yu’s *100 Days of Code* course. It demonstrates:
- For & While loops
- Conditional logic (if/elif/else)
- Working with strings and lists
- Range and the `random` module
- ASCII art for user experience

This project is sufficient to demonstrate all concepts, exercises, and tutorials taught in Day 7.

---

### 🔗 Links

- [Solution Code](./day06.py)
- [Original Course](https://www.udemy.com/course/100-days-of-code/)

---

## ⚙️ My Process

### 🧰 Built With

- Python
- External modules: `random`
- Files: `hangman_words.py`, `hangman_art.py`
- Terminal-based game interface

---

### 🧠 What I Learned

- How to use `for` and `while` loops effectively
- Nesting conditional statements with `if`, `elif`, `else`
- Handling user input in a game loop
- Working with lists to store and update character guesses
- Using ASCII art and modular file separation for better UX and cleaner code structure
- Improving basic UI experience with meaningful feedback and `clear()` function from `replit`

---

## 📝 Notes

- Enhanced the base code with customized messages based on remaining lives.
- Used modular structure (`hangman_words`, `hangman_art`) to manage word lists and stage graphics.
- Improved user experience with better input feedback and clearer visuals using the Replit `clear()` function.
