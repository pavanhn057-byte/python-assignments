import requests
from bs4 import BeautifulSoup

# Flipkart URL
url = "https://www.flipkart.com/search?q=mobiles"

# Headers to avoid blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Product containers
products = soup.find_all("div", class_="_1AtVbE")

for product in products:
    name = product.find("div", class_="_4rR01T")
    price = product.find("div", class_="_30jeq3 _1_WHN1")
    rating = product.find("div", class_="_3LWZlK")

    if name and price:
        print("Product Name:", name.text)
        print("Price       :", price.text)
        print("Rating      :", rating.text if rating else "No rating")
        print("-" * 50)
