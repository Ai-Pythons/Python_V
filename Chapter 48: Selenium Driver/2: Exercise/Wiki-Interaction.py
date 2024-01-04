from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 # options.add_argument(f'--user-agent={user_agent}')
 
driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# FInd element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# FInd the "Search" input by Name
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()