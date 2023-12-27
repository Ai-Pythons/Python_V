# Documentation
# - Selenium Elements: https://selenium-python.readthedocs.io/
# - 

from selenium import webdriver
from selenium.webdriver.common.by import By
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 # options.add_argument(f'--user-agent={user_agent}')
 
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

document_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").text
print(document_link)

# X-Path: https://www.w3schools.com/xml/xpath_intro.asp
job_link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[4]/p[2]/a').text

print(job_link)

driver.quit()

