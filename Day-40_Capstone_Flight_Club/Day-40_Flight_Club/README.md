# ✈️ Flight Club Program - Capstone Project

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![100DaysOfCode](https://img.shields.io/badge/100DaysOfCode-Python-green)

---

## 📝 Background

The **Flight Club Program** is a Capstone Project spanning two “Days” in the *100 Days of Code: Python* course.  

On the first day, one creates a Google Sheet containing a list of cities you want to visit. The code then checks that list and updates a column with the IATA codes for each destination (if missing).  

Next, the code searches for flights between the origin (LON) and each destination, updating the Google Sheet’s price column with the cheapest flight found.

On the second day, one creates a Google Form and attaches it to the aforementioned Google sheet. It let's users put in their info to join the Flight Club.

The returned data includes:  
- 💷 Price  
- ✈️ Origin and destination airports (IATA codes)  
- ⏱️ Number of stops  
- 📅 Departure and return dates  

Example output:  

> **Low price alert! Only £534.08 to fly from LGW to DPS, with 2 stop(s), departing on 2024-06-18 and returning on 2024-12-14.**

The lesson originally uses **Twilio** and multiple API calls to **Amadeus** and **Sheety**. In my implementation:  
- I use **requests-cache** to avoid rate limiting and speed up execution  
- Email notifications replace Twilio alerts for now  
- Twilio integration will be added in production  

---

## ✅ Program Requirements Summary

1. Retrieve the list of dream destinations from the Google Sheet via Sheety  
2. Check and update IATA codes for each destination via Amadeus  
3. Search for flight deals on Amadeus for departures starting **tomorrow** and up to **6 months** in the future  
4. Allow up to **2 stopovers** if no direct flights are available  
5. Return the cheapest flight for each trip, including:  
   - 💷 Price  
   - ✈️ From and to destinations (IATA codes)  
   - 📅 Departure and return dates  
   - Number of stop-overs, if any
6. Retrieve a list of email addresses from the Google Sheet  
7. Send a **price alert email** to each address with the flight details  

---

## 🛠️ Note about the Amadeus API

- The lesson uses **flight-offers-search**, which only returns flights between two specific dates.  
- Iterating multiple dates to find the absolute cheapest flights generates too many requests for a free plan.  
- Another API, **cheapest-flight**, would be perfect for the assignment however is limited on the trial version and leaves little control over requests.  

**Implementation decision:**  
- Stick with **flight-offers-search**  
- Assume the returned flights are the cheapest available  
- Always use departures **tomorrow** and returns **6 months later**  
- Future improvement: iterative date checks for more accurate pricing  

---

## ⚙️ Comment on Starting Code (Day 40)

- The starting code updates IATA codes but not flight prices  
- It attempts Twilio messages, but I use **email notifications** for easier testing  
- Twilio integration will come later  

---

## 🎉 Project Completion

- Challenge revisited: **August 19th**  
- Completion date: **August 25th**  

Despite daily life challenges, I dedicated significant effort to this project. Reviewing my solution, I am happy to see it aligns closely with the course’s expected implementation.  

**Outcome:** Successfully finishing this project represents a major milestone in my growth as a Python developer! 🚀

## Biggest Take-away
Sometimes returning an object is more efficient that returning a dictionary. With a dictionary you need to keep track of keys and length.
With an object, you can access its attributes with dot (.) notation easily.