import os
from dotenv import load_dotenv
from scraper.init import driver, By, Select

load_dotenv()


def authenticate():
    driver.get(os.getenv("BASE_URL"))

    # locating elements
    city = Select(driver.find_element(By.ID, "city"))
    username = driver.find_element(By.ID, "username")
    pwd = driver.find_element(By.ID, "password")
    submit = driver.find_element(By.XPATH, '//button[text()="Connexion"]')

    # inserting credentials
    city.select_by_value(os.getenv("CITY"))
    username.send_keys(os.getenv("USER"))
    pwd.send_keys(os.getenv("PASSWORD"))
    submit.click()
    return True
