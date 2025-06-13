# Day 32: Automated Happy Birthday Email

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I reviewed](#what-i-reviewed)

## Overview

This project covers all the Day 32 topics and is sufficient to demonstrate everything taught, including exercises and tutorials.

### The challenge

- Create an automated birthday greeting system using Python:
  - Read the `birthdays.csv` file.
  - Check if today’s date matches any birthday in the file.
  - If there is a match, select a random template letter and personalize it with the person's name.
  - Automatically send the birthday greeting to the person’s email.

## My process

### Built with

- Python

### What I reviewed

- Working with the `datetime` module to retrieve and format the current date.
- Reading and handling CSV data with `pandas`.
- Creating a dictionary from DataFrame rows using dictionary comprehensions.
- Randomly selecting and modifying text from `.txt` template files.
- Sending emails using the `smtplib` library and handling email server connections securely with `starttls()`.
