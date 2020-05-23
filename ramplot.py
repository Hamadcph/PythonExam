import matplotlib.pyplot as plt
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor

def ram_price_name():

    x = []
    y = []

    with open('ram.csv', 'r') as f:
        plots = pd.read_csv(f, skiprows=1, delimiter=',')
        for row in plots.values:
            y.append(str(row[0]))
            x.append(float(row[1]))


    plt.barh(y, x)

    plt.title('Name and price for ram')

    plt.xlabel('price')
    plt.ylabel('RamName')

    plt.show()

ram_price_name()
    
def ram_price_stars():

    x = []
    y = []

    with open('ram.csv', 'r') as f:
        plots = pd.read_csv(f, skiprows=1, delimiter=',')
        for row in plots.values:
            x.append(int(row[1]))
            y.append(float(row[2]))


    plt.bar(x, y)

    plt.title('Plot over numbers of stars and price')

    plt.xlabel('price')
    plt.ylabel('stars')

    plt.show()

    

ram_price_stars()

def ram_stars_name():
    x = []
    y = []

    with open('ram.csv', 'r') as f:
        plots = pd.read_csv(f, skiprows=1, delimiter=',')
        for row in plots.values:
            x.append(str(row[0]))
            y.append(float(row[2]))


    plt.barh(x, y)

    plt.title('Plot over numbers of stars and name')

    plt.xlabel('stars')
    plt.ylabel('name')

    plt.show()

ram_stars_name()

