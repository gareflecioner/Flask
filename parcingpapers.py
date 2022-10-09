import requests
from bs4 import BeautifulSoup
import sqlite3

url='https://www.womanandhome.com/life/books/the-25-best-books-of-all-time-for-your-must-read-listfrom-popular-fiction-to-classic-novels/'
response=requests.get(url)
soup=BeautifulSoup(response.content,"lxml")

def add(title,description):
    conn=sqlite3.connect("base.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO papers (title,description)
    VALUES(?,?)
    """ ,(title,description,) )

    conn.commit()

item=soup.find(id="article-body")
blocks=item.find_all("div",class_="featured_product_details_wrapper")

for block in blocks:
    title=block.find('div',class_="featured__title").text.strip()
    description=block.find("div",class_="subtitle__description").text.strip()

    add(title, description)
    print(title)
    print(description)
    print()




