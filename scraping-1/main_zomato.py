import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium.webdriver.common.by import By



headers = {
    'authority': 'scrapeme.live',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}  

driver = webdriver.Chrome(
    executable_path=r"C:\\Users\\Bhavya Yadav\\OneDrive\\Documents\\my projects\\chromedriver.exe")  
driver.get(
    "https://www.zomato.com/chennai/kfc-3-perambur/order")  
time.sleep(2)  
scroll_pause_time = 3  
screen_height = driver.execute_script("return window.screen.height;")  
i = 1

while True:  

    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height,
                                                                            i=i))  
    i += 1
    time.sleep(scroll_pause_time)

    scroll_height = driver.execute_script("return document.body.scrollHeight;")

    if (screen_height) * i > scroll_height:
        break  

soup = BeautifulSoup(driver.page_source, "html.parser")  
#print(soup.html)
divs=soup.findAll("div")
#print(divs)
divs1=soup.findAll('div','sc-1a03l6b-0 lkqupg')
divs2=soup.findAll('div','sc-1a03l6b-1 kvnZBD')
for i,x in enumerate(divs1):
    print("Coupon Number:",i)
    print("Coupon Names:",x.get_text())
for i,x in enumerate(divs2):
    print("Coupon Number:",i)
    print("Coupon Names:",x.get_text())