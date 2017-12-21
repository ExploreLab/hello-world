import time
import requests
from bs4 import BeautifulSoup

print("=======================================================")
print("| This application will show gold price int Thai Baht |")
print("|              for 10 seconds interval.               |")
print("=======================================================")

printCounter = 1
INTERVAL_TIME_IN_SECONDS = 10

def getGoldPrice():
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
    print(f"{printCounter}: {getGoldPrice()} THB.")
    printCounter += 1
    time.sleep(INTERVAL_TIME_IN_SECONDS)
