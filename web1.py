#web1.py

from bs4 import BeautifulSoup

page = open("C:\\work\\test01.html", "rt", encoding="utf-8")

soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#print(soup.find_all("p", attrs={class="outer-text"}))

print(soup.find_all(id="first"))

for tag in soup.find_all("p"):
    title = tag.text.strip()
#   title = title.replace("\n")
    print(title)

