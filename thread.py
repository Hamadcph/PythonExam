from selenium import webdriver
from bs4 import BeautifulSoup
from os import write
import time
from concurrent.futures import ThreadPoolExecutor



start = time.perf_counter()

driver = webdriver.Chrome()

def scrape_cpu(): 
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


def scrape_ram():
   with open('ram.csv', 'w') as f:
    f.write("RamName, price, rating \n")

    url = "https://www.komplett.dk/category/11209/hardware/pc-komponenter/hukommelse-ram?nlevel=10000%C2%A728003%C2%A711209&hits=100"
    driver.get(url)
    html = driver.page_source
    page_content = BeautifulSoup(html, features="lxml")

    with open('ram.csv', 'a') as f:

        for content_block in page_content.findAll("div", attrs={"class": "content-block"}):
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

# scrape_cpu()
# scrape_ram()
with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(scrape_cpu)
    future2 = executor.submit(scrape_ram)
    finish = time.perf_counter()
    #print(finish)




# t1 = threading.Thread(target=scrape_cpu)
# t2 = threading.Thread(target=scrape_ram)

# t1.start()
# t2.start()

# with threadpool: 3.3725512
# with threads: 5.5421385
# without threads: 6.0666078