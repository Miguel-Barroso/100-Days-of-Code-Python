# 100 Days of Code – Python

My progress through Dr. Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*. Each folder is one day; some include both the starter and my finished version.

## 📁 Structure

```
Day-XX_Project_Name/   # one folder per day (12–63 so far)
shared/                # reserved for cross-project helpers
Miscellaneous/         # course downloads, screenshots, scratch (gitignored)
```

Days 21 and 41–44 are intentionally absent — those bootcamp days covered HTML / CSS / JavaScript fundamentals, which I already knew from prior work. This repo is Python-only.

## 🐍 Setup

Single root virtual environment for the whole repo — no per-project venvs:

```bash
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
# .venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

`requirements.txt` lists every third-party package any project imports. Run all `Day-XX` scripts from this activated venv.

## 🔑 Secrets

All API keys, tokens, and credentials live in per-project `.env` files (already gitignored). Each affected project loads them via `python-dotenv`.

## 📊 Project status (2026)

The course was written in 2020. Some third-party services have changed their free tiers or shut down APIs since then. This table tracks what still works as-is.

| Day | Project | Status | Notes |
|----:|---------|:------:|-------|
| 12 | Scope & Number Guessing Game | ✅ | Standalone |
| 13 | Debugging exercises | 🐛 | Code is *intentionally* buggy — fixing it is the exercise |
| 14 | Higher Lower Game | ✅ | Standalone |
| 15 | Coffee Machine | ✅ | Standalone |
| 16 | OOP Coffee Machine | ✅ | Standalone |
| 17 | OOP Quiz | ✅ | Standalone |
| 18 | Turtle & GUI | ✅ | Standalone (turtle) |
| 19 | Higher-Order Functions | ✅ | Standalone (turtle) |
| 20 | Snake Game | ✅ | Standalone (turtle) |
| 22 | Snake — Inheritance | ✅ | Standalone (turtle) |
| 23 | Turtle Crossing Capstone | ✅ | Standalone (turtle) |
| 24 | Files, Directories, Paths | ✅ | Standalone |
| 25 | CSV & Pandas | ✅ | Standalone |
| 26 | NATO Alphabet | ✅ | Standalone |
| 27 | Tkinter — args/kwargs | ✅ | Standalone (tkinter) |
| 28 | Pomodoro GUI | ✅ | Standalone (tkinter) |
| 29 | Password Manager GUI | ✅ | Standalone (tkinter) |
| 30 | Password Manager + JSON | ✅ | Standalone (tkinter) |
| 31 | Flash Card Capstone | ✅ | Standalone (tkinter) |
| 32 | Birthday Email Sender | 🔑 | Gmail SMTP app password |
| 33 | ISS Overhead Alert | 🔑 | Open-Notify (free) + Gmail SMTP |
| 34 | Quiz App (API) | ✅ | Open Trivia DB — still free |
| 35 | Rain Alert | 🔑 | OpenWeatherMap (free) + Twilio trial |
| 36 | Stock & News Alert | ⚠️ | Alpha Vantage = 25 req/day in 2026; NewsAPI free is dev-only |
| 37 | Pixela Habit Tracker | 🔑 | Pixela — still free |
| 38 | Workout Tracking | 🔑 | Nutritionix + Google Sheets API |
| 39 | Flight Deal Finder | ⚠️ | Original Tequila/Kiwi API discontinued — Day 40 swapped to Amadeus |
| 40 | Flight Club Capstone | 🔑 | Amadeus self-service API (still has free tier) |
| 45 | Beautiful Soup intro | ✅ | Hacker News scrape |
| 46 | Musical Time Machine | 🔑 | Spotify Web API (OAuth) |
| 47 | Amazon Price Tracker | ⚠️ | Selectors break frequently; bring-your-own User-Agent |
| 48 | Selenium intro | ✅ | Practice exercises |
| 49 | Automated Gym Booker | ⚠️ | Site-specific Selenium — selectors likely rotted |
| 50 | Tinder Swiper | ⚠️ | Tinder actively blocks automation |
| 51 | Twitter ISP Complaint | ⚠️ | Twitter API free tier killed in 2023; Selenium login still works at your own risk |
| 52 | Instagram Followers | ⚠️ | Instagram aggressively blocks bots; educational only |
| 53 | Data Entry Capstone | ⚠️ | Zillow + Google Forms — Zillow selectors change often |
| 54 | Flask intro | ✅ | Local dev server |
| 55 | Higher Lower (Flask) | ✅ | Local dev server |
| 56 | Render HTML & static files | ✅ | Local dev server |
| 57 | Jinja templating | ✅ | Local dev server |
| 58 | Bootstrap foundation | ✅ | Static HTML/CSS |
| 59 | Upgraded Blog | ✅ | Local dev server |
| 60 | Flask POST / HTML forms | 🔑 | Gmail SMTP for contact form |
| 61 | Flask-WTF Forms | ✅ | Local dev server |
| 62 | WTForms + Bootstrap + CSV | ✅ | Local dev server |
| 63 | SQLite + SQLAlchemy | ✅ | Local dev server + sqlite file |

**Legend:** ✅ runs standalone &nbsp;·&nbsp; 🔑 needs API keys / credentials &nbsp;·&nbsp; ⚠️ depends on a service that changed or broke since 2020 &nbsp;·&nbsp; 🐛 intentionally buggy (learning exercise)

## 🔁 Workflow

```
git pull
# work on code
git add .
git commit -m "Day XX: description"
git push
```

## 🚫 Ignored Files

- Virtual environments (`.venv/`)
- IDE settings (`.idea/`)
- Large media files (`.mov`, `.mp4`, etc.) and compressed archives
- Databases (`*.sqlite3`)
- `.env` files
- Build artifacts (`build/`, `dist/`, `*.spec`, `*.app/`)
- Selenium browser profiles (`chrome_profile/`)
- Course downloads and scratch (`Miscellaneous/`)

## 🎯 Goal

Build consistency, improve problem-solving, and develop real-world Python skills.
