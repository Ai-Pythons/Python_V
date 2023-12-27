from selenium import webdriver
from selenium.webdriver.common.by import By
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)
 # options.add_argument(f'--user-agent={user_agent}')
 
driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event = {}

for n in range(len(event_times)):
    event[n] = {
        "time": event_times[n].text,
        "name": event_name[n].text,
    }
print(event)

driver.quit()