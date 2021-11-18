from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
s = Service("/home/lynne/Programs/Development/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element(By.XPATH, "//*[@id='bigCookie']")
timeout = time.time() + 10  # 60*5 5 minutes from now
five_secs = time.time() + 5
prices_list = []
while True:
    cookie.click()
    if time.time() > five_secs:
        all_prices = driver.find_elements(By.CLASS_NAME, "price")
        for price in all_prices:
            #To get the price
            price = price.get_attribute('innerHTML')
            prices_list.append(price)
            five_secs = time.time() + 5
    print(prices_list)

    if time.time() > timeout:
        break

