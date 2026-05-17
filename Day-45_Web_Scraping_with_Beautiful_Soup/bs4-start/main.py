from bs4 import BeautifulSoup

with open('website.html', 'r') as website:
    content = website.read()
    # print(content)

soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())  # Prints the whole html page in a structured format
# print(soup.title)  # Access the (first) title tag as a Python object
# print(soup.title.string)  # Access the contents between the title tags
# print(soup.a) # Returns the first anchor tag it finds
# all_anchor_tags = soup.find_all(name='a')  # Access all anchor tags and return as a list
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())  # Get all text of the anchor tags
#     print(tag.get('href'))  # Get all URLs

# heading = soup.find_all(name='h1')
# heading = soup.find(name='h1', id='name')  # Finds the first h1 it finds with the id 'name'
# print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')  # 'class' is reserved keyword in Python, use class_
# print(section_heading.get('class'))
#
# company_url = soup.select_one(selector='p a')  # Query to select an anchor tag nested within a p tag
# print(company_url)
#
# name = soup.select_one(selector='#name')  # Any CSS selector works, like the id in this case, returns one
# print(name)
#
# headings = soup.select('.heading')  # Selecting all elements with the class of heading
# print(headings)

