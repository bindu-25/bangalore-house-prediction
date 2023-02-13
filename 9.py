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
url = "https://www.magicbricks.com/Property-Rates-Trends/ALL-RESIDENTIAL-rates-in-Bangalore"
driver.get(url)
driver.refresh()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "price-trends-tables")))

products = []

product = driver.find_elements(By.CLASS_NAME, "price-trends-tables")

for p in product:
    print(p.text)
    #a = p.find_elements(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[3]/div[1]/div/div[2]/table/tbody/tr[3]/td[2]")#title
    #for elem in a:
    #    print("Title",elem.text)

