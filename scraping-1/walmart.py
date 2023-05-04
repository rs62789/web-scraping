import requests
from bs4 import BeautifulSoup

url = 'https://www.zomato.com/mumbai/sabir-bhais-veera-desai-area/order'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section that contains the offers
offers_section = soup.find('div', {'class': 'sc-1a03l6b-2 gerWzu'})

# Extract all the offers
offers = offers_section.find_all('div', {'class': 'sc-1a03l6b-0 lkqupg'})

# Print the offers
for offer in offers:
    print(offer.text.strip())
