---

2024-10-04

The program requirements state:

    "In this project, we're looking only for non-stop flights that leave anytime between tomorrow and six months (6x30 days)
    from now. We're also looking for round trips for 1 adult. The currency of the price returned should be in GBP."

Together with many of my fellow students, I interpret this as:

    "Find the cheapest*, non-specified duration trip that can start anytime from tomorrow until six months from now."
    (*"Cheapest" is mentioned in other parts of the program requirements but not explicitly here.)

However, the suggested "Amadeus Flight Offers Search API" cannot search across a range of dates. You can specify a
start and end date for the query, but this will only return a trip with the specified dates.

This limitation led me to consider making multiple API calls in a loop, expanding the range of dates incrementally.
While this is possible, it would quickly exceed the monthly quota of 2000 API calls. Considering that the application
is meant to check flights for a list of cities in a Google Sheet, this approach is not feasible.

There is another API offered by Amadeus, called "Cheapest Flight", which does check a range of flights between two
specified dates. However, there is a caveat: the available origins and destinations are limited, likely because the
data is cached, and presumably only for popular routes. Here's a related StackOverflow discussion:
[Flight Offers Search and Flight Cheapest Date Search - Limitation by Number of Connections](https://stackoverflow.com/questions/62869019/flight-offers-search-and-flight-cheapest-date-search-limit-by-number-of-connec)

This raised the question of which API is actually used in the solution provided here:
[Flight Data Search Code](https://gist.github.com/TheMuellenator/2ebb13d348c4a91b4ab27d1fd3627fb0)

Upon reviewing the code, and confirming with ChatGPT, it appears that the original "Flight Offers Search API"
is being used. This API, however, does **not** return flights with arbitrary durations within the specified date range.
It only returns the cheapest flight for a specific pair of departure and return dates.

From reading the comments, it's clear that many students struggled with this part of the project. It seems that the
lesson was updated recently without fully considering the current limitations of the API. Furthermore, the video
lessons were replaced with static text, but they fail to address the exact challenge the students are facing.

### My Modified Solution:

In my solution, I aim to find the cheapest "two-week trip" to the specified destinations using the original
"Flight Offers Search API". The program will:
1. Check flight trips departing tomorrow and returning 14 days later.
2. Increment the departure date by 14 days + 1, so as not to include the end day of one trip, i.e.:
    If trip_start = 2020-01-01, then trip_end = 2020-01-15 and next trip_start = 2020-01-16
3. Repeat this process 12 times since floor(180 days / 14 days) = 12 iterations.

For the 9 destination cities in the Google Sheet, there will be a total of 108 (9 * 12) queries done each time the
program runs and the cheapest dates and price for each will be updated in the sheet.
---