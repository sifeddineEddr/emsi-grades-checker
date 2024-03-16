import time
from scraper.init import driver, By, WebDriverWait, EC


def bring_grades():
    modules = driver.find_element(By.CLASS_NAME, "col").find_elements(
        By.CLASS_NAME, "card"
    )

    for index, module in enumerate(modules):
        try:
            title = module.find_element(By.TAG_NAME, "h5").text

            # click the toggle button
            module.find_element(By.CLASS_NAME, "details-btn").click()

            module_details = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, f"moduleDetails-{index}"))
            )

            module_avg = (
                module_details.find_element(By.CLASS_NAME, "moyenne-label")
                .find_element(By.TAG_NAME, "span")
                .text
            )

            print(f"{title} - {module_avg}")
            time.sleep(5)
        except Exception as e:
            print(f"Error {e}")
