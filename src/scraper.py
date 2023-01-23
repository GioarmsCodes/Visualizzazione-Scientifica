'''

Il seguente codice sorgente non è quello che è stato utilizzato effettivamente per il progetto:
- queste funzioni rappresentano le 3 modalità con le quali abbiamo "scrapato" i dati:
  - tag "table" che contiene tag "tr"
  - tag "div" che contiene tag "div"
  - tag "div" che contiene tag "tr"
- i dati estratti non venivano stampati a video ma venivano salvati in file CSV per facilitarne lo scambio

I dati, presi dal file "data.txt", sono nel formato ENDPOINT:ID, dove:
- ENDPOINT rappresenta appunto l'endpoint al quale viene fatta la richiesta HTTP
- ID rappresenta l'id del contenitore che contiene i dati da estrarre

'''

import requests
from bs4 import BeautifulSoup as bs


def scraper_table(endpoint : str, id_ : str) -> None:
    data = bs(requests.get(endpoint).text, "html.parser")
    data = data.find("table", id=id_)
    for row in data.find_all("tr"):
        label = row.find("td", class_="label").text.strip()
        value = row.find("span").text.strip()
        print(f"{label} : {value}")
    print()


def scraper_div_div(endpoint : str, id_ : str) -> None:
    data = bs(requests.get(endpoint).text, "html.parser")
    data = data.find("div", id=id_)
    for row in data.find_all("div", class_="bar-row"):
        label = row.find_all("div", class_="bar-label")[0].text.strip()
        value = row.find_all("div", class_="bar-label")[1].text.strip()
        print(f"{label} : {value}")
    print()


def scraper_div_tr(endpoint : str, id_ : str):
    data = bs(requests.get(endpoint).text, "html.parser")
    data = data.find("div", id=id_)
    for row in data.find_all("tr"):
        label = row.find("td", class_="label").text.strip()
        value = row.find("span").text.strip()
        print(f"{label} : {value}")
    print()


with open("../data.txt", "r") as f:
    first, second, third = f.read().strip().split("\n\n")

for row in first.strip().split("\n"):
    end,id_ = row.split(";")
    scraper_table(end, id_)

for row in second.strip().split("\n"):
    end,id_ = row.split(";")
    scraper_div_div(end, id_)

for row in third.strip().split("\n"):
    end,id_ = row.split(";")
    scraper_div_tr(end, id_)
