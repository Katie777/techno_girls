from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome('drivers/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# click Help
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_help')]").click()

# search by cancel order
search = driver.find_element(By.XPATH, "//input[@type='search']")
search.clear()
search.send_keys('cancel order')

# Click Go
driver.find_element(By.ID, 'helpSearchSubmit').click()

#Verify that 'Cancel Items or Orders’ text is present
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[contains(@class, 'a-box-inner')]").text

# print out element's text into console
print(driver.find_element(By.XPATH, "//div[contains(@class, 'help-content')]").text)

driver.quit()










