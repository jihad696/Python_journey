# Selenium Automation Cheat Sheet & Example Scripts

This repository contains Selenium automation scripts along with a beginner-friendly cheat sheet to help you understand how Selenium works.

---

## Selenium Modules

- `selenium.webdriver` → Controls and interacts with the browser.
- `Service` → Tells Selenium where the browser driver is located.
- `Options` → Set browser options like Brave or headless.
- `By` → Methods to locate elements (ID, CSS_SELECTOR, XPATH, etc.).
- `WebDriverWait` → Waits for a condition to be true before continuing.
- `expected_conditions as EC` → Predefined conditions to wait for, like element visibility or presence.
- `ChromeDriverManager` → Automatically manages the correct ChromeDriver version.

---

## Locators

- `By.ID`, `By.NAME`, `By.CLASS_NAME`, `By.TAG_NAME`, `By.LINK_TEXT`, `By.PARTIAL_LINK_TEXT`, `By.CSS_SELECTOR`, `By.XPATH`

---

## Waits

- `EC.presence_of_element_located(locator)` → Waits until a single element exists in the DOM.
- `EC.presence_of_all_elements_located(locator)` → Waits until all matching elements exist in the DOM.
- `EC.visibility_of_element_located(locator)` → Waits until a single element is visible.
- `EC.visibility_of_all_elements_located(locator)` → Waits until all matching elements are visible.
- `EC.element_to_be_clickable(locator)` → Waits until an element is visible and clickable.
- `EC.text_to_be_present_in_element(locator, text)` → Waits until the element contains the specified text.
- `EC.staleness_of(element)` → Waits until a specific element is removed from the DOM.

---

## Example Scripts

- `wikipedia_search.py` → Search Wikipedia and print first paragraph.
- `python_news_brave.py` → Scrape 5 latest Python news (Brave browser).

---

### How to Run

1. Install dependencies:

```bash
pip install selenium webdriver-manager
```

2. Run scripts:

```bash
python examples/wikipedia_search.py
python examples/python_news_brave.py
```

3. Notes:

- Make sure your scripts are inside the `examples/` folder.
- For the Brave browser script, ensure Brave is installed and update the `brave_path` variable if needed.
- You can also use Chrome without changing anything in `wikipedia_search.py`.

---

## Folder Structure

```
Python_Selenium_Projects/
├─ README.md                  # Cheat sheet + instructions
├─ examples/                  # Folder for working Selenium scripts
│   ├─ wikipedia_search.py    # Wikipedia search example (Chrome)
│   └─ python_news_brave.py   # Python.org news scraper (Brave)
├─ requirements.txt           # Selenium & WebDriver dependencies
```
