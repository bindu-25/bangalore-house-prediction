import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=&cityName=Bangalore&category=B&parameter=rel&hideviewed=N&ListingsType=I&filterCount=3&incSrc=Y&fromSrc=homeSrc"
response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


cards = soup.find_all("div", class_="mb-srp__list")


data = []


for card in cards:
    card_data = {}
    card_data["title"] = card.find("h2").text
    data.append(card_data)



df = pd.DataFrame(data)


print(df)

df.to_csv('dataset1.csv')
