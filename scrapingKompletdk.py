from selenium import webdriver
from bs4 import BeautifulSoup
import re
from os import write

driver = webdriver.Chrome()

with open('ram.csv', 'w') as f:
    f.write("RamName, price \n")

    url = "https://www.komplett.dk/category/11209/hardware/pc-komponenter/hukommelse-ram?nlevel=10000%C2%A728003%C2%A711209&hits=2000"
    driver.get(url)
    html = driver.page_source
    content = BeautifulSoup(html)

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

    for x in content.findAll("div", attrs={"class": "content-block"}):
        names = x.findAll("a", attrs={"class": "product-link"})
        prices = x.findAll("div", attrs={"class": "product-price"})
        # print(names)
        for name, price in zip(names, prices):
            n = name.findAll("h2")
            p = price.findAll("span")
            for finalPrice, finalName in zip(p, n):
                f.write(finalName.text + "," + finalPrice.text + "\n")
