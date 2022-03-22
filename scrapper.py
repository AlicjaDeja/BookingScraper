import requests
from bs4 import BeautifulSoup

url = "https://www.booking.com/hotel/gb/avonmore-london.en-gb.html?auth_success=1#tab-reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("li.review_list_new_item_block")
review = reviews.pop()
print(review)
