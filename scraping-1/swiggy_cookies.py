import pickle
from selenium import webdriver

# Open the website in the browser and let the user manually log in
url = "https://www.swiggy.com/"
driver = webdriver.Chrome()
driver.get(url)
input("Please log in to the website and press Enter to continue...")

# Extract the cookies from the session
cookies = driver.get_cookies()

# Store the cookies in a file using pickle
with open("cookies_swiggy.pkl", "wb") as f:
    pickle.dump(cookies, f)
