import requests
from bs4 import BeautifulSoup
import sqlite3

url='https://www.womanandhome.com/life/books/the-25-best-books-of-all-time-for-your-must-read-listfrom-popular-fiction-to-classic-novels/'
response=requests.get(url)
soup=BeautifulSoup(response.content,"lxml")

def add(title,description,market,price):
    conn=sqlite3.connect("instance/again.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO papers (title,description,market,price)
    VALUES(?,?,?,?)
    """ ,(title,description,market,price,) )

    conn.commit()

item=soup.find(id="article-body")
nazvanie=item.find_all("div",class_="featured_product_details_wrapper")
cena=item.find_all("div",class_="featured_product_block featured_block_hero")

#title = nazvanie.find_all('div', class_="featured__title").text.strip()
#description = nazvanie.find_all("div", class_="subtitle__description").text.strip()
#market=cena.find_all('a',class_="hawk-affiliate-link-merchantlink-label").text.strip()
#price = cena.find_all('div', class_="hawk-display-price-price")

#print(title)
#print(description)
#print(market)
#print(price)


#for block in nazvanie:
    #title=block.find('div',class_="featured__title").text.strip()
    #description=block.find("div",class_="subtitle__description").text.strip()
    #print(title)
    #print(description)
    #add(title,description)
#for i in cena:
    #market=i.find('a',class_="hawk-affiliate-link-merchantlink-label").text.strip()
    #price = i.find('div', class_="hawk-display-price-price")
    #add(title,description,market,price)
    #add(market,price)
    #print(market)
    #print(price)



