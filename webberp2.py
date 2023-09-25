import time 
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# animename = str(input())

browser = Firefox()
browser_action = ActionChains(browser)
browser.get("https://animepahe.ru")
time.sleep(3)

# > stage 1: Navigate the browser to the download page for animepahe
def pahe_search():
    animepahe_search = browser.find_element(By.CSS_SELECTOR, ".input-search")
    animepahe_search.click()
    animepahe_search.send_keys('jobless reincarnation')
    time.sleep(1)
    anime = browser.find_element(By.CSS_SELECTOR, ".search-results > li:nth-child(1) > a:nth-child(1)")
    anime.click()

try:
    pahe_search()
except:
    print(browser.current_window_handle, type(browser.current_window_handle))
    if browser.current_window_handle == 0:
        pahe_search()
    else:
        browser.switch_to.window(browser.window_handles[0])
        pahe_search()

pahe_episode = browser.find_element(By.CSS_SELECTOR, "div.episode-wrap:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4)")
try:
    browser_action.scroll_to_element(pahe_episode)
    pahe_episode.click()
except:
    if browser.current_window_handle != 0:
        browser.switch_to.window(browser.window_handles[0])
        browser_action.scroll_to_element(pahe_episode).perform()
        pahe_episode.click()
        time.sleep(1)

def find_ele(selector=str()):
    browser. find_element(By.CSS_SELECTOR, selector)
    browser.click()

try:
    find_ele(selector='#downloadMenu')
except:
    if browser.current_window_handle == 0:
        find_ele('#downloadMenu')
    else:
        browser.switch_to(browser.window_handles[0])
        find_ele('#downloadMenu')

try:
    find_ele()
except:
    if browser.current_window_handle == 0:
        find_ele()
    else:
        find_ele()

# > stage 2: Navigate the browser to the download page for pahewin
try:
    find_ele()
except:
    browser.switch_to.window(browser.window_handle[1])
    time.sleep(6)
    find_ele()

# > stage 3: navigate the browser to the download page of kwik
try:
    find_ele()
except:
    browser.switch_to.window(browser.window_handle[1])
    find_ele()

# 
browser.current_url
browser.window_handles
browser.get_window_position()
browser.set_page_load_timeout(10)
browser.current_url
browser.window_handles