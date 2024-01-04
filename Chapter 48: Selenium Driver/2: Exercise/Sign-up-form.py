from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 # options.add_argument(f'--user-agent={user_agent}')
 
driver = webdriver.Chrome(options=options)
driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

# FInd the "Search" input by Name
fName = driver.find_element(By.NAME, "fName")
fName.send_keys("akun", Keys.ENTER)

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("tumbal", Keys.ENTER)

email = driver.find_element(By.NAME, "email")
email.send_keys("akuntumbal@gmail.com", Keys.ENTER)

sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()

# driver.quit()