import requests
from bs4 import BeautifulSoup
import sqlite3

url='https://www.womanandhome.com/life/books/the-25-best-books-of-all-time-for-your-must-read-listfrom-popular-fiction-to-classic-novels/'
response=requests.get(url)
soup=BeautifulSoup(response.content,"lxml")

def add(title,description,market,price):
    conn=sqlite3.connect("base.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO papers1 (title,description,market,price)
    VALUES(?,?,?,?)
    """ ,(title,description,market,price,) )

    conn.commit()

item=soup.find(id="article-body")
nazvanie=item.find_all("div",class_="featured_product_details_wrapper")
cena=item.find_all("div",class_="featured_product_block featured_block_hero")

for block in nazvanie:
    title=block.find('div',class_="featured__title").text.strip()
    description=block.find("div",class_="subtitle__description").text.strip()
    print(title)
    print(description)

for i in cena:
    market=i.find('a',class_="hawk-affiliate-link-merchantlink-label").text.strip()
    price = i.find('span', class_="hawk-display-price-price")
    add(title,description,market,price)

    print(market)
    print(price)



