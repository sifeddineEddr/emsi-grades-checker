import time
from scraper.init import driver
from utils.auth import authenticate
from utils.navigate import navigate
from utils.grades import bring_grades

while True:
    try:
        if authenticate():
            print("Authenticated")
            for term in range(0, 2):
                if navigate(term):
                    print(f"Term {term+1}:")
                    bring_grades()
                    with open("grades.json", "r") as file:
                        data = file.read()

                        # cheching if the file is not empty
                        if data.strip():
                            driver.quit()
                            break
                    print("Retrying...")
            print("Scraping process completed")
    except Exception as e:
        time.sleep(5)
