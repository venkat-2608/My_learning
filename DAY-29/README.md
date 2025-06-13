# Day 29: Project - Password Manager 1.0

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Create a Password Manager GUI using Tkinter with the following features:
  - Generate secure passwords
  - Copy password to clipboard automatically
  - Input fields for website, email, and password
  - Save entered credentials to a text file
  - Use messagebox for validations and confirmations

## My process

### Built with

- Python
- Tkinter
- Pyperclip
- Random Module

### What I learned

This project covers all the Day 29 topics and is sufficient to demonstrate everything taught, including exercises and tutorials.

- Reviewed Tkinter basics and UI design
- Added images using `PhotoImage()` and displayed on `Canvas`
- Used `grid()` for layout with `columnspan` for wider buttons
- Implemented pop-up windows using `messagebox.showinfo()` and `askokcancel()`
- Used list comprehensions to generate strong passwords with letters, numbers, and symbols
- Applied `join()` method to convert password lists into strings
- Handled file operations using `with open()` in append mode
- Copied generated passwords to clipboard using `pyperclip.copy()`
- Used `.get()`, `.insert()`, `.delete()` to manage Entry widgets
- Set focus to input field with `.focus()`
