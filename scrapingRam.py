import re
from os import write

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

with open('ram.csv', 'w') as f:
    f.write("RamName, price, rating \n")

    url = "https://www.komplett.dk/category/11209/hardware/pc-komponenter/hukommelse-ram?nlevel=10000%C2%A728003%C2%A711209&hits=100"
    driver.get(url)
    html = driver.page_source
    content = BeautifulSoup(html, features="lxml")

with open('ram.csv', 'a') as f:
    # for x in content.findAll("a", attrs={"class": "product-link"}):
    #     names = x.findAll("h2")
    #     for name in names:
    #         print(name.text)
    #        # f.write(name.text + "\n")

    # for x in content.findAll("div", attrs={"class": "product-price"}):
    #     prices = x.findAll("span")
    #     for price in prices:
    #         print(price.text)
    #         #f.write(name.text + "\n")

    for content_block in content.findAll("div", attrs={"class": "content-block"}):
        names = content_block.findAll("a", attrs={"class": "product-link"})
        prices = content_block.findAll("div", attrs={"class": "product-price"})
        products_review = content_block.findAll("div", attrs={"class": "review"})

        # print(names)
        for name, price, rating in zip(names, prices, products_review):
            n = name.findAll("h2")
            p = price.findAll("span")
            r = rating.findAll("span", attrs={"class": "rating-stars"})

            for finalPrice, finalName, finalRating in zip(p, n, r):
                f.write(finalName.text + "," + finalPrice.text + "," + finalRating["title"] + "\n")
