import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

path = r"C:\Users\KingED\Downloads\geckodriver-v0.33.0-win-aarch64\geckodriver.exe"
webber = Firefox()

# goes to animepahe.ru website
webber.get("https://animepahe.ru")

# inserts anime name on the search tab
search = webber.find_element(By.NAME, "q")
search.click()
search.send_keys("jobless reincarnation")
time.sleep(5)

# clicks the first anime on the list
anime = webber.find_element(By.XPATH, '/html/body/header/nav/div/form/div/ul/li[1]/a')
anime.click()

# 
episode_actions = ActionChains(webber)
episode = webber.find_elements(By.CSS_SELECTOR, 'div.episode-wrap:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4)')
episode_actions.click(on_element=episode).perform()
