from bs4 import BeautifulSoup
import requests

# Make a request to the website
url = "https://www.magicbricks.com/owner-property-for-sale-in-bangalore-pppfs"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the elements with class "mb-srp__card"
cards = soup.find_all('div', class_='mb-srp__card')

# Extract data from each card
for card in cards:
    title = card.find('div', class_='mb-srp__title').text
    location = card.find('div', class_='mb-srp__location').text
    price = card.find('div', class_='mb-srp__price').text
    print(title)
    print(location)
    print(price)
