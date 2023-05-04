import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Initialize the web driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://www.zomato.com/")

# Wait for the user to manually log in
input("Please log in manually and press enter to continue...")

# Retrieve the cookies from the current session
cookies = driver.get_cookies()

# Close the web driver
driver.quit()

# Print the cookies
for cookie in cookies:
    print(cookie)
