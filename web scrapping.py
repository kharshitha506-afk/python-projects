import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes
    quotes = soup.find_all("span", class_="text")

    # Print all quotes
    print("Quotes from the website:\n")
    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote.text}")
else:
    print("Failed to retrieve the website")
