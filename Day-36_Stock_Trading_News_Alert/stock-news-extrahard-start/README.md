# Stock News

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📖 Description
Fetches the most recent closing price and the previous closing price of 
a list of stocks. The percent difference is evaluated and if above a threshold,
the top three latest news headlines for each company are sent as either SMS (Twilio) or
or as an email to the user.

## 🚀 Features
- Alpha Vantage API connection to fetch the two most recent closing prices
- News API to fetch the three latest news for each company
- API calls are cached, so you can send messages to more users if needed with the same info
- Choose between SMS or email notifications

## 📦 Installation
```bash
pip install -r requirements.txt
