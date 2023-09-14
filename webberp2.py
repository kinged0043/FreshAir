import time 
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# animename = str(input())

browser = Firefox()
browser_action = ActionChains(browser)
browser.get("https://animepahe.ru")
time.sleep(3)

# > part 1: Navigate the browser to the download page for animepahe
def pahe_search():
    animepahe_search = browser.find_element(By.CSS_SELECTOR, )
    animepahe_search.click()
    animepahe_search.send_keys('jobless reincarnation')
    anime = browser.find_element(By.CSS_SELECTOR, )
    anime.click()
    time.sleep(2)

try:
    pahe_search()
except:
    print(browser.current_window_handle, type(browser.current_window_handle))
    if browser.current_window_handle == 0:

        pahe_search()
    else:
        browser.switch_to.window(browser.window_handles[0])
        pahe_search()

try:
    pahe_episode = browser.find_element(By.CSS_SELECTOR, )
    browser_action.scroll_to_element(pahe_episode)
    pahe_episode.click()
    time.sleep(2)
except:
    browser.switch_to.window(browser.window_handle[0])
    browser.find_element(By.CSS_SELECTOR, )
    browser_action.scroll_to_element(pahe_episode).perform()
    pahe_episode.click()
    time.sleep(2)

# > part 2: Navigate the browser to the download page for pahewin
try:
    pahewin = browser.find_element(By.CSS_SELECTOR, )
    pahewin.click()
    
except:
    browser.switch_to.window(browser.window_handle[1])
    time.sleep(6)
    pahewin.click()

# > part 3: navigate the browser to the download page of kwik
try:
    kwik = browser.find_element(By.CSS_SELECTOR, )
    kwik.click()
except:
    browser.switch_to.window(browser.window_handle[2])
    kwik.click()

# 
browser.current_url
browser.window_handles
browser.get_window_position()
browser.set_page_load_timeout(10)