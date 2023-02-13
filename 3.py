from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create an instance of the Firefox driver
driver = webdriver.Firefox(executable_path=r'D:\github\HelloWorld\geckodriver.exe')

# Navigate to the Magicbricks website
driver.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Hyderabad")

# Wait for the page to load and the card elements to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mb-srp__title")))

# Find all the card elements by class name
cards = driver.find_elements_by_class_name("mb-srp__title")

# Loop through the card elements and extract the desired data
for card in cards:
    title = card.find_element_by_class_name("mb-srp__card--title").text
    print(title)

