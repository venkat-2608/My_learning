# Day 24 Project – Mail Merge: Automated Letter Generator

This project covers all the Day 24 topics and is sufficient to demonstrate everything taught, including exercises and tutorials.

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful Resources](#useful-resources)

## Overview

### The challenge

- Create a letter using `starting_letter.txt`.
- For each name in `invited_names.txt`:
  - Replace the `[name]` placeholder in the letter with the actual name.
  - Save the personalized letter in the folder `ReadyToSend/` with the filename format: `letter_for_<name>.txt`.

## My process

### Built with

- Python

### What I learned

- How to use `with open()` to read and write files.
- Difference between absolute and relative file paths.
- How to use `readlines()` to loop through file contents line-by-line.
- How to use `replace()` to dynamically substitute placeholders with actual data.
- How to use `strip()` to clean newline characters from file content.

### Useful Resources

- 📄 [Readlines Method](https://www.w3schools.com/python/ref_file_readlines.asp)
- 🔤 [String Replace() Method](https://www.w3schools.com/python/ref_string_replace.asp)
- ✂️ [String Strip() Method](https://www.w3schools.com/python/ref_string_strip.asp)
