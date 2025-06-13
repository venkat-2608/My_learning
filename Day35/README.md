# Day 35: Rain Alert App

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

This project demonstrates all key concepts taught up to this point, including working with external APIs, environment variables, and message automation using third-party services.

### The challenge

- Build an app that alerts you when it is raining.
- Instead of Twilio, use Telegram to send alerts and stickers.

## My process

- The original requirement was to send a message via Twilio, but I switched to Telegram to send messages.
- Added functionality to send a rain cloud sticker using Telegram bot API.
- Explored Telegram documentation deeply to understand message and sticker sending and learned how to find chat IDs and authenticate bots.

### Built with

- Python
- OpenWeather API
- Telegram Bot API
- Latitude and Longitude geolocation

### What I learned

- How to use external APIs and pass parameters
- API keys and authentication management via environment variables
- Sending messages and stickers using Telegram bot
- JSON parsing and slicing data for specific timeframes
