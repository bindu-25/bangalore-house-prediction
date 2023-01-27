import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the website
url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=&cityName=Bangalore&category=B&parameter=rel&hideviewed=N&ListingsType=I&filterCount=3&incSrc=Y&fromSrc=homeSrc"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the cards on the page
cards = soup.find_all("div", class_="mb-srp__list")

# Create an empty list to store the data
data = []

# Extract the data from the cards
for card in cards:
    card_data = {}
    card_data["title"] = card.find("h2").text
    data.append(card_data)


# Create a data frame from the list
df = pd.DataFrame(data)

# Print the data frame
print(df)

df.to_csv('dataset1.csv')