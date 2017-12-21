import time
import requests
from bs4 import BeautifulSoup

Gval = 1
def getPriceGBBuy():
    r = requests.get("https://www.goldtraders.or.th/")
    soup = BeautifulSoup(r.content, "html.parser")
    data = soup.find_all("span", {"id": "DetailPlace_uc_goldprices1_lblBLBuy"})
    for i in range(len(data)):
        # print(data[i].text)
        GBBuy = data[i].text

    b = "!@,,#$"
    for char in b:
        GBBuy = GBBuy.replace(char, "")
    return GBBuy

while 1:
    Gval = getPriceGBBuy()
    print(Gval)
    time.sleep(6)