from selenium import webdriver
from bs4 import BeautifulSoup
import re
from os import write

driver = webdriver.Chrome()

with open('cpu.csv', 'w') as f:
    f.write("CpuName, price, rating \n")

    url = "https://www.komplett.dk/category/11204/hardware/pc-komponenter/processorer?nlevel=10000%C2%A728003%C2%A711204&hits=100"
    driver.get(url)
    html = driver.page_source
    page_content = BeautifulSoup(html, features="lxml")

with open('cpu.csv', 'a') as f:

    for content_block in page_content.findAll("div", attrs={"class": "content-block"}):
        products_info = content_block.findAll("a", attrs={"class": "product-link"})
        products_price = content_block.findAll("div", attrs={"class": "product-price"})
        products_review = content_block.findAll("div", attrs={"class": "review"})
        #print(names)
        
        for name, price, rating in zip(products_info, products_price, products_review):

            n = name.findAll("h2")
            p = price.findAll("span")
            r = rating.findAll("span", attrs={"class": "rating-stars"})
            for finalPrice, finalName, finalRating in zip(p, n, r):
                f.write(finalName.text + "," + finalPrice.text +  "," + finalRating["title"] + "\n")
