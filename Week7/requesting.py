import requests
from bs4 import BeautifulSoup
import re
from Histogram import Histogram
import matplotlib.pyplot as plt


url = "http://register.start.bg"
custom_url = "http://register.start.bg/link.php?id="
r = requests.get(url)
soup = BeautifulSoup(r.text)
ids = []
custom_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
h = Histogram()
symbols = ["/", "-", "\\"]
for row in soup.find_all("a"):
    if isinstance(row.get("href"), str) and row.get("href")[:4] == "link":
        ids.append(row.get("href")[-5:])
for x in range(40, 50):
    try:
        rr = requests.get(
            custom_url + str(ids[x]), headers=custom_header, timeout=1)
        server = dict(rr.headers)["server"]
        print (server)
        if "/" in server:
            position = server.find("/")
            h.add_server(server[:position])
        else:
            h.add_server(server)
    except Exception:
        print("cant connect to site !")

h = h.get_dict()
keys = list(h.keys())
values = list(h.values())

X = list(range(len(keys)))

plt.bar(X, list(h.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")

plt.savefig("histogram.png")
