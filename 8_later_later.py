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
driver.refresh()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "mb-srp__card")))

products = []

product = driver.find_elements(By.CLASS_NAME, "mb-srp__card")

for p in product:

    a = p.find_elements(By.CLASS_NAME,"mb-srp__card--title")#title
    for elem in a:
        print("Title",elem.text)
        products.append(elem.text)
    a = p.find_elements(By.CLASS_NAME,"mb-srp__card__society")#society
    for elem in a:
        print("Society",elem.text)
        products.append(elem.text)
    a = p.find_elements(By.CLASS_NAME,"mb-srp__card__ads--name")#Owner
    for elem in a:
        print("Owner",elem.text)
        products.append(elem.text)
    a = p.find_elements(By.CLASS_NAME,"mb-srp__card__summary__list")#Area
    for elem in a:
        print("Details",elem.text)
        products.append(elem.text)

print(products)