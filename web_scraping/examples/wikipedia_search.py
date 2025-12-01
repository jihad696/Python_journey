from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# before that you have to use "pip install selenium" and this is code work for only chrome browser
options = Options()
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://www.wikipedia.org/")

browser.find_element(By.ID, "searchInput").send_keys("Selenium (software)")
browser.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)

first_paragraph = browser.find_element(By.CSS_SELECTOR, "p").text
print(first_paragraph)

browser.quit()
