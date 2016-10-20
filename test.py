import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 0
    while page <= max_pages:
        page_url="https://www.google.com/?gws_rd=ssl#q=test&start=" + str(page)
        source_code = requests.get(page_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a"):
          #  href = link.get("href")
            print(link)
        page += 10

trade_spider(1)