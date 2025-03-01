from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os

load_dotenv()
session_value = os.getenv("SESSION_VALUE")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://stake.us/?tab=dailyBonus&currency=btc&modal=wallet')


# Proper cookie format: {"name": "session", "value": "-", "domain": ".stake.us"},
if session_value:
    driver.add_cookie({"name": "session", "value": session_value, "domain": ".stake.us"})

# Refresh the page to apply cookies
driver.refresh()

# Ensures components are loaded
time.sleep(3)

# Find Submit
# Locate the button based on the text inside the div

form_element = driver.find_element(By.CSS_SELECTOR, "form.svelte-188ba96")
# attempts to grab numbers left until daily claim
# nums = driver.find_element(By.CLASS_NAME, "digits svelte-1gvsbmk")
submit = form_element.find_element(By.CSS_SELECTOR, "button[type='submit'][data-test='password-reset-button'] div.contents")

if submit.is_enabled():
    print("The button is clickable.")
else:
    print("The button is disabled.")

time.sleep(1000)