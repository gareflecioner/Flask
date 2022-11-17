import requests
from bs4 import BeautifulSoup
import sqlite3

url='https://www.radiox.co.uk/features/best-vinyl-records-to-collect/'
response=requests.get(url)
soup=BeautifulSoup(response.content,"lxml")

def add(title,description):
    conn=sqlite3.connect("again.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO vinyl (title,description)
    VALUES(?,?)
    """ ,(title,description,) )

    conn.commit()

item=soup.find(id="cadmus-article_31734")
blocks=item.find_all("li",class_="collection__item")

for block in blocks:
    title=block.find("h2",class_="title").text.strip()
    description=block.find("p",class_="paragraph-text").text.strip()

    add(title, description)
    # вызываю функцию и определяю переменные
    print(title)
    print(description)
    print()




