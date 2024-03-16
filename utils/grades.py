import time
import json
from scraper.init import driver, By, WebDriverWait, EC, ActionChains


def scroll_to_element(element):
    actions = ActionChains(driver)
    actions.scroll_to_element(element).perform()


def bring_grades():
    data = list()

    modules = driver.find_element(By.CLASS_NAME, "col").find_elements(
        By.CLASS_NAME, "card"
    )

    for index, module in enumerate(modules):
        sub_data = list()
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
        sub_modules = module_details.find_element(By.TAG_NAME, "tbody").find_elements(
            By.TAG_NAME, "tr"
        )
        for sub_module in sub_modules:
            texts = sub_module.find_elements(By.TAG_NAME, "td")
            sub_data.append({texts[0].text: texts[1].text})

        time.sleep(3)
        details_dropdown.click()

        data.append(
            {
                "module": title,
                "average": module_avg,
                "sub_modules": sub_data,
            }
        )

    with open("grades.json", "w") as file:
        json.dump(data, file)
