from linkedin_scraper import Person, actions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3")

# username = "sashopigas@gmail.com"
# password = "Sasho1234"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

import time

username = "sashopigas@gmail.com"
password = "Sasho1234"

driver.get("https://www.linkedin.com/")
time.sleep(300)
