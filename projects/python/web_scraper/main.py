import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h1").text

print(title)