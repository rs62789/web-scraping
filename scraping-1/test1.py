# Import necessary libraries
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import datetime


# Get the file path from the user
file_path = "C:\\Users\\Bhavya Yadav\\OneDrive\\Documents\\my projects\\scraping\\cookies.pkl"

# Load the cookies from the file using pickle
with open(file_path, "rb") as f:
    cookies = pickle.load(f)

# Set options for the webdriver
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')

# Open the website using the extracted cookies
url = "https://www.zomato.com/"
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.delete_all_cookies()
for cookie in cookies:
    driver.add_cookie({
        "name": cookie["name"],
        "value": cookie["value"],
        "domain": cookie["domain"]
    })
driver.refresh()

# Wait for the page to load
time.sleep(random.uniform(1, 3))

# Read the Excel file to get the URLs
df = pd.read_excel("C:\\Users\\Bhavya Yadav\\OneDrive\\Documents\\my projects\\scraping\\Discounts Tracker.xlsx", sheet_name="Sheet1")

# Extract the URLs from the relevant rows in the Excel sheet
urls = []
for url in df["Zomato URL"]:
    if "zoma.to/r/" in url:
        urls.append("https://www." + url.replace("https://", "").split("?")[0])
    else:
        urls.append(url)

# Scrape each URL
for i, url in enumerate(urls):
    # Load the URL
    driver.get(url)

    # Wait for the page to load
    time.sleep(random.uniform(1, 3))

    try:
        # Find the element to click
        order_button = driver.find_element_by_link_text('Order Online')

        # Click the element
        order_button.click()

        # Wait for the page to load
        time.sleep(7)

        # Extract the HTML content
        html = driver.page_source

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Find all the coupon codes on the page
        coupon_codes = []
        discounts = []
        for coupon in soup.find_all("div", class_="sc-1a03l6b-2 gerWzu"):
            coupon_codes.append(coupon.find("div", class_="sc-1a03l6b-0 lkqupg").text)
            discounts.append(coupon.find("div", class_="sc-1a03l6b-1 kvnZBD").text)

        # If there are no coupon codes found, print "Restaurant is closed"
        if not coupon_codes:
            print("Restaurant is closed for " + url)
        else:
            # Print the coupon codes
            print("Coupons for " + url + ":")
            print(coupon_codes)
            print(discounts)
            print()

        # Write the coupon codes and discounts to the Excel sheet
        for j, coupon_code in enumerate(coupon_codes):
            df.at[i, f"Zomato Code - {j+1}"] = coupon_code
        for j, discount in enumerate(discounts):
            df.at[i, f"Zomato construct - {j+1}"] = discount

    except NoSuchElementException:
        print("Order Online button not found for " + url)
        continue

    # Add a column for the date and time when the scraping is done
    now = datetime.datetime.now()
    df.at[i, "Scraping Date"] = now.strftime("%Y-%m-%d")
    df.at[i, "Scraping Time"] = now.strftime("%H:%M:%S")

    # Wait for a random amount of time before proceeding to the next URL
    time.sleep(random.uniform(1, 3))

# Save the results to the Excel file and quit the webdriver
df.to_excel("C:\\Users\\Bhavya Yadav\\OneDrive\Documents\\my projects\\scraping\\Discounts Tracker.xlsx", index=False)
print("Excel file saved successfully!")

driver.quit()


