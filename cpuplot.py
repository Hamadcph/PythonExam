import matplotlib.pyplot as plt
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor



def cpu_price_name():

    x = []
    y = []

    with open('cpu.csv', 'r') as f:
        plots = pd.read_csv(f, skiprows=1, delimiter=',')
        for row in plots.values:
            y.append(str(row[0]))
            x.append(float(row[1]))


    plt.barh(y, x)

    plt.title('Name and price for cpu')

    plt.xlabel('price')
    plt.ylabel('cpuName')

    plt.show()

cpu_price_name()
    
def cpu_price_stars():

    x = []
    y = []

    with open('cpu.csv', 'r') as f:
        plots = pd.read_csv(f, skiprows=1, delimiter=',')
        for row in plots.values:
            x.append(int(row[1]))
            y.append(float(row[2]))


    plt.bar(x, y)

    plt.title('Plot over numbers of stars and price')

    plt.xlabel('price')
    plt.ylabel('stars')
    bottom, top = plt.ylim()
    plt.ylim(bottom=0)
    plt.ylim(top=5)
    left, right = plt.xlim()
    plt.xlim(left=100)
    plt.xlim(right=1200)
    plt.show()

cpu_price_stars()

def cpu_stars_name():
    x = []
    y = []

    with open('cpu.csv', 'r') as f:
        plots = pd.read_csv(f, skiprows=1, delimiter=',')
        for row in plots.values:
            x.append(str(row[0]))
            y.append(float(row[2]))


    plt.barh(x, y)

    plt.title('Plot over numbers of stars and name')

    plt.xlabel('stars')
    plt.ylabel('name')

    plt.show()

cpu_stars_name()


