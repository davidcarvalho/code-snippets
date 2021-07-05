import requests
from bs4 import BeautifulSoup
import re

r = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
soup = BeautifulSoup(r.content, 'lxml')

text = soup.prettify().split("<!--")[1].split("-->")[0]


m = re.match("^\w+", text)

print(m.groups())