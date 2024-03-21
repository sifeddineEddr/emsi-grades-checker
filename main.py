import sys
import time
from scraper.init import driver
from utils.auth import authenticate
from utils.navigate import navigate
from utils.grades import bring_grades

if __name__ == "__main__":
    while True:
        try:
            term = int(sys.argv[1]) - 1  # 0 indexed
            if authenticate():
                print("Authenticated")
                if navigate(term):
                    print(f"Term {term+1}:")
                    bring_grades()
                    with open("grades.json", "r") as file:
                        data = file.read()

                        # cheching if the file is not empty
                        if data.strip():
                            print("Scraping process completed")
                            driver.quit()
                            break
            print("Retrying...")
        except Exception as e:
            time.sleep(5)
