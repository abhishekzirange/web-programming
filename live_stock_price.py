import requests
from bs4 import BeautifulSoup


def stock_price(symbol):
    url = "https://in.finance.yahoo.com/quote/"+symbol
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px)"
    return soup.find("div", class_=class_).find("span").text


if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
        print("Current ",symbol," stock price is ",stock_price(symbol))
