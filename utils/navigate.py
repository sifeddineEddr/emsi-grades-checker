from scraper.init import driver, By, WebDriverWait, EC


def navigate(term):
    grades_dropdown = driver.find_element(By.XPATH, "//li[@class='nav-item dropdown']")
    terms = grades_dropdown.find_elements(By.XPATH, ".//ul[@class='dropdown-menu']//a")

    grades_dropdown.click()

    link = WebDriverWait(driver, 10).until(EC.visibility_of(terms[term]))
    if "disabled" in link.get_attribute("class"):
        print(f"{terms[term].text} disabled")
        return False
    else:
        link.click()
        return True
