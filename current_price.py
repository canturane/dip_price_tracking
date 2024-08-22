import requests
from bs4 import BeautifulSoup as bs
import time

prices = []

while True:
    url = "https://crypto.com/price/shrapnel-com"
    headers = {
        # user-agent you can find your current User-Agent string by searching for "my user agent" on Google.
        "User-Agent": ""
    }

    page = requests.get(url, headers=headers)
    soup = bs(page.content, "lxml")

    blazer = soup.find_all("span", {"class": "chakra-text css-13hqrwd"})
    # print(blazer)

    for i in blazer:
        current_price = i.get_text(strip=True)
        prices.append(current_price)

    # print(prices)

    if len(prices) >= 2:
        if prices[-1] < min(prices[:-1]):
            print("Price dropped: " + str(prices[-1]))
        else:
            print("Current price: " + str(prices[-1]))
    else:
        print("Not enough data for price tracking.")
    print("************************")
    time.sleep(10)
