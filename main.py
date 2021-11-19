from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
global unlocked
s = Service("/home/lynne/Programs/Development/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element(By.XPATH, "//*[@id='bigCookie']")
timeout = time.time() + 60*5
five_secs = time.time() + 5
products = driver.find_elements(By.CSS_SELECTOR, "#products")
product_ids = [product.get_attribute("id") for product in products]
while True:
    cookie.click()
    if time.time() >= five_secs:
        for each in product_ids:
            unlocked_products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            # print(unlocked_products)
            prices_list = [int(element.text.split()[1]) for element in unlocked_products]
            cookies = driver.find_element(By.ID, "cookies").text.split()[0]
            cookies_count = int(cookies)
            # print(cookies)
            # to get most expensive upgrade that is affordable
            affordable_upgrade = [None]
            for price in prices_list:
                if price <= cookies_count:
                    affordable_upgrade[0] = price
            affordable_product = str(affordable_upgrade[0])
            for product in unlocked_products:
                unlocked = product.text
                if affordable_product in unlocked:
                    product.click()
        five_secs = time.time() + 5

    if time.time() > timeout:
        break

