from scraper.init import driver
from utils.auth import authenticate
from utils.navigate import navigate
from utils.grades import bring_grades

if authenticate():
    print("Authenticated")
    for term in range(0, 2):
        if navigate(term):
            print(f"Term {term+1}:")
            bring_grades()
    print("done")
driver.quit()
