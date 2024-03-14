import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


try:
    chrome_options = Options()
    chrome_options.headless = False
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-notifications")
    driver = uc.Chrome(options=chrome_options)

except Exception as e:
    print(f"Error: {e}")
