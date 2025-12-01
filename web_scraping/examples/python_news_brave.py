from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Path to Brave browser
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

options = Options()
options.binary_location = brave_path

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://www.python.org/")

news_items = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.blog-widget li"))
)

for item in news_items[:5]:
    date = item.find_element(By.TAG_NAME, "time").text
    title = item.find_element(By.TAG_NAME, "a").text
    print(f"{date} -> {title}")

browser.quit()
