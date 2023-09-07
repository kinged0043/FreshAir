import time
import script
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

path = r"C:\Users\KingED\Downloads\geckodriver-v0.33.0-win-aarch64\geckodriver.exe"
webber = Firefox()
action = ActionChains(webber)

# goes to animepahe.ru website
webber.get("https://animepahe.ru")

# inserts anime name on the search tab
search = webber.find_element(By.NAME, "q")
search.click()
search.send_keys("jobless reincarnation")
time.sleep(2.5)

# clicks the first anime on the list
anime = webber.find_element(By.XPATH, '/html/body/header/nav/div/form/div/ul/li[1]/a')
time.sleep(2)
anime.click()

#episode =webber.find_element(By.LINK_TEXT, "Watch - 12 Online")
time.sleep(2)
episode = webber.find_element(By.CLASS_NAME, "episode-snapshot")
episode.click()

url_num = webber.window_handles.count
print(url_num)

download_button = webber.find_element(By.XPATH, '//*[@id="downloadMenu"]')
download_button.click()
webber.switch_to.window(webber.window_handles[0])
download_720 = webber.find_element(By.XPATH, '/html/body/section/article/div/div/div[2]/div/div[4]/div/div/a[3]')
download_720.click()

next_page = webber.find_element(By.CLASS_NAME, 'btn btn-primary btn-block redirect')
next_page.click()
time.sleep(6)

webber.switch_to.window(webber.window_handles[1])

winx = webber.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/div[2]/div[2]/form/button')
webber.switch_to.windoe(webber.window_handles[1])
