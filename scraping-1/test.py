import pickle
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

# Get the file path from the user
file_path = "C:\\Users\\Bhavya Yadav\\OneDrive\\Documents\\my projects\\scraping\\cookies.pkl"

# Load the cookies from the file using pickle
with open(file_path, "rb") as f:
    cookies = pickle.load(f)

# Set options for the webdriver
options = webdriver.ChromeOptions()
options.headless = False
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
urls = ["https://" + str(x) for x in df["Zomato URL"].apply(lambda x: "zoma.to/r/" + str(x)).tolist()]

# Scrape each URL
# Scrape each URL
for url in urls:
    # Load the URL
    driver.get(url.replace("https://", "https://www."))

    # Wait for the page to load
    time.sleep(random.uniform(1, 3))
    
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
    valids = []
    for coupon in driver.find_elements_by_xpath("//div[contains(@class, 'sc-1a03l6b-3') and contains(@class, 'GyojG') and contains(@class, 'sc-ibCXtz') and contains(@class, 'ceTKts')]"):

        # Click the coupon element to open it
        coupon.click()

        # Wait for the coupon to open
        time.sleep(5)

        # Extract the coupon details
        discount = driver.find_element_by_class_name("sc-cCbPEh.jggGUw").text
        valid = driver.find_element_by_class_name("sc-eklfrZ.ctZzau").text
        coupon_code = driver.find_element_by_class_name("sc-1hez2tp-1.sc-cLmFfZ.eSyMcR").text



        # Add the coupon details to the lists
        coupon_codes.append(coupon_code)
        discounts.append(discount)
        valids.append(valid)
        driver.refresh()

        # Wait for the page to load
        time.sleep(8)


    # If there are no coupon codes found, print "Restaurant is closed"
    if not coupon_codes:
        print("Restaurant is closed for " + url)
    else:
        # Print the coupon codes
        print("Coupons for " + url + ":")
        print(coupon_codes)
        print(valids)
        print(discounts)
        print()

    # Wait for a random amount of time before proceeding to the next URL
    time.sleep(random.uniform(1, 3))

# Close the driver
driver.quit()
