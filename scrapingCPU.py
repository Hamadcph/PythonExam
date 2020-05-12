from selenium import webdriver
from bs4 import BeautifulSoup
import re
from os import write

driver = webdriver.Chrome()

with open('cpu.csv', 'w') as f:
    f.write("CpuName, price \n")

    url = "https://www.komplett.dk/category/11204/hardware/pc-komponenter/processorer?nlevel=10000%C2%A728003%C2%A711204&hits=2000"
    driver.get(url)
    html = driver.page_source
    content = BeautifulSoup(html)

with open('cpu.csv', 'a') as f:

    for x in content.findAll("div", attrs={"class": "content-block"}):
        names = x.findAll("a", attrs={"class": "product-link"})
        prices = x.findAll("div", attrs={"class": "product-price"})
        #print(names)
        for name, price in zip(names, prices):
            n = name.findAll("h2")
            p = price.findAll("span")
            for finalPrice, finalName in zip(p, n):
                f.write(finalName.text + "," + finalPrice.text + "\n")
