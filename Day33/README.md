# Day 33: ISS Overhead Notifier Project

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

This project covers all the Day 33 topics and is sufficient to demonstrate everything taught, including exercises and tutorials.

### The challenge

- Track the International Space Station (ISS) and determine if it’s overhead at night.
- If the ISS is close to the current location and it’s dark outside, send an email notification.

## My process

### Built with

- Python
- ISS location tracking API
- Sunrise-sunset API
- SMTP for sending emails

### What I learned

- Making API calls with `requests`
- Working with API parameters and endpoints
- Parsing and using JSON responses
- Handling time with the `datetime` module
- Automating periodic checks using `time.sleep()`
- Sending emails using `smtplib`
- Writing conditional logic based on location and time
