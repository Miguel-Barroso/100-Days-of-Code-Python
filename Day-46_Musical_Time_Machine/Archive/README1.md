The Billboard Hot 100 website was accessed on 2025-08-29.
The selectors for the song names was really complicated.
It was not enough to select all h3 with an id of #title-of-a-story and a class of .c-title.

What I had to do was to open developer tools (in Firefox) and run this command:

document.querySelectorAll('div.o-chart-results-list-row-container:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(1) > li:nth-child(1) > h3:nth-child(1)')

I got the query by inspecting a song name and copying its CSS selector.

The console gave this output:

NodeList [ h3#title-of-a-story.c-title.a-font-basic.u-letter-spacing-0010.u-max-width-397.lrv-u-font-size-16.lrv-u-font-size-14@mobile-max.u-line-height-22px.u-word-spacing-0063.u-line-height-normal@mobile-max.a-truncate-ellipsis-2line.lrv-u-margin-b-025.lrv-u-margin-b-00@mobile-max ]

I had to strip away classes with @ in their names but managed to sucessfully grab all song names with this command:

songs = billboard_hot100.select('h3#title-of-a-story.c-title.a-font-basic.u-letter-spacing-0010.u-max-width-397.lrv-u-font-size-16.u-line-height-22px.u-word-spacing-0063.a-truncate-ellipsis-2line.lrv-u-margin-b-025')

This took a while of digging around the documentation but I got the most help from:

https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-returns-empty-list/#step-1-check-if-response-contains-data

Where they told me about document.querySelectorAll('h1') and that you could use developer tools to effectively select css selectors for bs4.

Another thing to mention that the response contains rendered html. This resulted in a lot of blank spaces before and after the song names.
To strip away them I used the get_text(strip=True) function of bs4. It effectively removed any rendered blank spaces but kept the song names intact.

Also, remember to use response.content and not response.text in order to get the correct text encoding.

