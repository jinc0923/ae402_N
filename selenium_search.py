import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 使用模擬enter鍵的話需要import的
# from selenium.webdriver.common.keys import Keys 

chrome = webdriver.Chrome()
chrome.get('https://www.google.com')
inputBar = chrome.find_element(By.CLASS_NAME, 'gLFyf')
inputBar.send_keys('猿創力')
time.sleep(1)

# 模擬按下enter鍵
# inputBar.send_keys(Keys.ENTER)
chrome.find_element(By.CLASS_NAME, 'gNO89b').click()
time.sleep(1)

chrome.find_element(By.PARTIAL_LINK_TEXT, "猿創力程式設計學校").click()
time.sleep(1)


#全螢幕
chrome.maximize_window()
#截圖
chrome.get_screenshot_as_file('codingApe.png')
