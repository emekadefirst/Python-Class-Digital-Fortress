from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
url = "https://www.selenium.dev/documentation/webdriver/getting_started/first_script/"
driver.get(url)
print(f"{url} has been opened by driver")


# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# title = driver.title

# driver.implicitly_wait(0.5)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

# driver.quit()
