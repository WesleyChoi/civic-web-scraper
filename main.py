# Press Shift+F10 to execute it or replace it with your code.

import requests

from bs4 import BeautifulSoup

# URL = desired URL
URL = "https://vancouver.craigslist.org/d/for-sale/search/van/sss?query=civic%20si&sort=rel"

page = requests.get(URL)
# print(page.content)


# parse rows from page
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="rows")
# print(results.prettify())

# parse cars from rows
car_elements = results.find_all('li', class_="result-row")

for car_elem in car_elements:
    print(car_elem.text)