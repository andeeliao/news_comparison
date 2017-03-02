import requests
from bs4 import BeautifulSoup

fox_page = requests.get("http://www.foxnews.com/")

fox_soup = BeautifulSoup(fox_page.content, "html.parser")

fox_soup.select("div.primary")