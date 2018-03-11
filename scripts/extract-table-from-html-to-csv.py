from bs4 import BeautifulSoup
import urllib2
import csv
from path import path


filename = '../docs/documents/registered-allied-professionals-11-3-2018.htm'
html = path(filename).bytes()
soup = BeautifulSoup(html, "html5lib")
table = soup.select_one("table.customReportsTable")
# python3 just use th.text
headers = [th.text.encode("utf-8") for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])