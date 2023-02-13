from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

firefox_options = Firefox_Options()
firefox_options.binary = r'C:\Program Files\Mozilla Firefox\firefox.exe';
driver = webdriver.Firefox(executable_path=r'D:\github\HelloWorld\geckodriver.exe',options=firefox_options)
url = "https://www.magicbricks.com/owner-property-for-sale-in-bangalore-pppfs"
driver.get(url)

# Wait for the page to load and the card elements to appear 
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mb-srp__card")))

cont = driver.find_elements(By.CLASS_NAME, "mb-srp__card")

for p in cont:
    title = p.text
    print(title)