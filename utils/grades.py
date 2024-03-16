import time
from scraper.init import driver, By, WebDriverWait, EC, ActionChains


def scroll_to_element(element):
    actions = ActionChains(driver)
    actions.scroll_to_element(element).perform()


def bring_grades():
    modules = driver.find_element(By.CLASS_NAME, "col").find_elements(
        By.CLASS_NAME, "card"
    )

    for index, module in enumerate(modules):
        scroll_to_element(module)

        title = module.find_element(By.TAG_NAME, "h5").text

        details_dropdown = module.find_element(By.CLASS_NAME, "details-btn")
        scroll_to_element(details_dropdown)
        details_dropdown.click()

        module_details = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, f"moduleDetails-{index}"))
        )

        module_avg = (
            module_details.find_element(By.CLASS_NAME, "moyenne-label")
            .find_element(By.TAG_NAME, "span")
            .text
        )
        time.sleep(3)
        details_dropdown.click()
        print(f"{title} - {module_avg}")
