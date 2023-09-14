import time 
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = Firefox()
browser.get("https://www.datacamp.com")
browser_action = ActionChains(browser)

email = 
password = 
# login section 
browser.find_element(By.CLASS_NAME, )
browser.send_keys(email)
browser.find_element(By.CLASS_NAME, )
browser.send_keys(password)
browser.find_element(By.CLASS_NAME, )
browser.click()
time.sleep(6)

# navigate to the course/track of choice
# note you can use find_elements to get all elements that contain videos in a course for easier download
# and you can probably fetch the names of the videos and store them in a list