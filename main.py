import time
from scraper.init import driver
from utils.auth import authenticate
from utils.navigate import navigate

# while True:
if authenticate():
    print("Authenticated")
    for term in range(0, 2):
        if navigate(term):
            print("Navigated")
driver.quit()
