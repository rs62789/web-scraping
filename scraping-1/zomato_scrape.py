from selenium import webdriver
from bs4 import BeautifulSoup
import time

urls = ["https://www.zomato.com/chennai/mcdonalds-kilpauk/order", 
        "https://www.zomato.com/chennai/kfc-3-perambur/order"]

# Initialize the Selenium driver
path = 'C:\\Users\\Bhavya Yadav\\OneDrive\\Documents\\my projects\\chromedriver.exe'
driver = webdriver.Chrome(path)

for url in urls:
    # Load the URL
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Extract the HTML content
    html = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all the coupon codes on the page
    coupon_codes = []
    disk = []
    for coupon in soup.find_all("div", class_="sc-1a03l6b-2 gerWzu"):
        coupon_codes.append(coupon.find("div", class_="sc-1a03l6b-0 lkqupg").text)
        disk.append(coupon.find("div", class_="sc-1a03l6b-1 kvnZBD").text)

    # Print the coupon codes
    print("Coupons for " + url + ":")
    print(coupon_codes)
    print(disk)
    print()

# Close the driver
driver.quit()
