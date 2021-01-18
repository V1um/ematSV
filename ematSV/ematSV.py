from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium
import subprocess
import time
import getpass

username = input('USERNAME: ')
password = getpass.getpass('PASSWORD: ')


delay = 3

url = "https://www.emat.dk"
tab_url = 'https://emat1.dk/resultat.aspx'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver_path = driver

driver.get(url)

# login button
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_ImageButton_UNILogin"))
    )
    element.click()

except:
    NoSuchElementException

# unilogin
time.sleep(2)
driver.refresh()

username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)

time.sleep(1)
username_textbox.send_keys(Keys.RETURN)

password_textbox = driver.find_element_by_id("form-error")
password_textbox.send_keys(password)
time.sleep(1)
password_textbox.send_keys(Keys.RETURN)

# View træningsopgaver
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "ctl00_ImageButton_VisSendteTrOpgaver"))
    )
    element.click()

except:
    NoSuchElementException

time.sleep(1)
# -------------------------------------------------------------------------------------------
# OPGAVE ID
# -------------------------------------------------------------------------------------------
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, "ctl00_ContentPlaceHolder1_28044"))  # Id på opgaven skal stå her i ""
    )
    element.click()

except:
    NoSuchElementException
# -------------------------------------------------------------------------------------------
# OPGAVE ID
# --------------------------------------------------------------------------------------------

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.ID, "ctl00_ContentPlaceHolder1_ImageButton_Start"))
    )
    element.click()

except:
    NoSuchElementException

time.sleep(1)


# New tab

driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])
driver.get(tab_url)


# Switch back to the first tab with URL A
# browser.switch_to.window(browser.window_handles[0])
