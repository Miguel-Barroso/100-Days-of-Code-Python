Here's a tidied-up version of your text:

---

**2024-10-25**

Today, I’ve decided to conclude this project (v2) for the following reasons:

My program cycles through the cities, IATA codes, and the lowest prices recorded in the Google Sheet, updating missing
values in the latter two columns to prevent errors.

It then iterates through a list of IATA codes, searching for a 14-day trip starting tomorrow and incrementing the start
date in 15-day intervals up to 180 days in the future. This effectively finds the cheapest 14-day return flight
available within the next six months.

This functionality exceeds what the App Brewery's solution code provides, which I downloaded and modified for testing.

While their code is better structured according to OOP principles, it only checks for one return flight with a start
date of tomorrow and a return date six months from now. This does not align with the goal of finding the cheapest
flight, as I have confirmed by running my code and comparing the results with the solution code.

If I were to make amendments to my code, I would focus on updating the Google Sheet with the cheapest price found
(something App Brewer's solutions does not). Achieving this would require better structuring my code according to OOP
principles, specifically by calling and returning method calls in `main.py` instead of within some of my methods.

I’ve spent considerable time solving this problem, even though the App Brewery team has not done a great job with
this lesson:

- The program requirements are not fulfilled by their code.
- The video lesson has been removed in favor of a barely useful text explanation (albeit with pictures).
- This is supposed to be a capstone project building on previous lessons, but it turned out to be filled with pitfalls
due to inadequate instruction on setting up OOP properly.
- There are typos in the solution code (e.g., `TWILIO_VIRTUAL_NUMBER` is used as both From and To in the notification
manager).
- The frustration of many other students is evident from the numerous comments on Udemy and GitHub.

In conclusion, my code executes well according to the program requirements. I have studied the solution code thoroughly
and hope to apply this knowledge in future lessons.