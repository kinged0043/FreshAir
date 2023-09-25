import time 
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

browser = Firefox()
browser_action = ActionChains(browser)
browser.get("https://animepahe.ru")
time.sleep(3)

# > stage 1: Navigate the browser to the download page for animepahe
def pahe_search():
    animepahe_search = browser.find_element(By.CSS_SELECTOR, ".input-search")
    animepahe_search.click()
    animepahe_search.send_keys("jobless reincarnation")
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
    else:
        browser_action.scroll_to_element(pahe_episode)
        time.sleep(1)
        pahe_episode.click()

download = browser.find_element(By.CSS_SELECTOR, '#downloadMenu')
p1080 = browser.find_element(By.CSS_SELECTOR, "#pickDownload > a:nth-child(3)")
try:
    download.click()
except:
    if browser.current_window_handle == 0:
        download.click()
        time.sleep(1)
        p1080.click()
    else:
        browser.switch_to.browser.window_handles[0]
        download.click()
        if browser.current_window_handle != 0:
            browser.switch_to.browser.window_handles[0]
            p1080.click()
        else: p1080.click

try:
    browser
except:
    if browser.current_window_handle == 0:
        browser
    else:
                

# > stage 2: Navigate the browser to the download page for pahewin

try:
    browser.find_element(By.CSS_SELECTOR)
except:
    browser.switch_to.window(browser.window_handle[1])
    time.sleep(6)
    

# > stage 3: navigate the browser to the download page of kwik
try:
    browser
except:
    browser.switch_to.window(browser.window_handle[1])
    