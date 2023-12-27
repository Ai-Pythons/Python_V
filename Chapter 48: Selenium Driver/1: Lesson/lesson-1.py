# Documentation
# - Selenium Elements: https://selenium-python.readthedocs.io/
# - 

from selenium import webdriver
from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent
 
# ua = UserAgent()
# user_agent = ua.random
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
# options.add_argument(f'--user-agent={user_agent}')
 
driver = webdriver.Chrome(options=options)
 
driver.get("https://www.amazon.com/dp/B0BSHF7WHW")
 
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

price_all = float(price_dollar.replace('$', '').replace(',', ''))
 
print(f"The Price is {price_dollar} / {price_all}")


driver.quit()

