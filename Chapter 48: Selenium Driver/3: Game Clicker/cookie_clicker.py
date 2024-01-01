
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

CLICKABLE = "rgba(238, 238, 238, 1)"
end = time.time() + 60 * 5

def automatic_click(seconds):
    cookie = driver.find_element(By.ID, "cookie")
    t_end = time.time() + seconds
    while time.time() < t_end:
        cookie.click()
        time.sleep(0.001)
 
def buy_best():
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    for item in reversed(store):
        if item.value_of_css_property("background-color") == CLICKABLE:
            item.click()
            break

while time.time() < end:
    automatic_click(5)
    buy_best()

cookie_per_s = driver.find_element(By.ID, "cps").text
print(cookie_per_s)
time.sleep(5)