import requests

url = "https://www.booking.com/hotel/gb/avonmore-london.en-gb.html"
response = requests.get(url)
print(response.status_code)
print(response.text)