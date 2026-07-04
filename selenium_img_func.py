from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests


search = input('想要下載甚麼照片?')
chrome = webdriver.Chrome()
chrome.get('https://pic.sogou.com')
time.sleep(1)

def download(search):
    inputBar = chrome.find_element(By.CLASS_NAME, "query.query-defalut")
    inputBar.send_keys(search)
    inputBar.send_keys(Keys.ENTER)
    time.sleep(0.5)
    chrome.maximize_window()
    time.sleep(0.5)
    for i in range(2):
        chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(1)
    i=1
    for element in chrome.find_elements(By.CSS_SELECTOR, 'img'):
        try:
            img_url = element.get_attribute('src')
            imgRespond = requests.get(img_url) # except
            with open(str(i)+".jpg","wb") as file:
                file.write(imgRespond.content)
                print("done")
            if i ==200:
                break
            i+=1
        except:
            print("Failed to Download")
    time.sleep(0.5)
    chrome.close()

download(search)