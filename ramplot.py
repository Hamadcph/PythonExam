import matplotlib.pyplot as plt
import pandas as pd

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

#plot: der viser sammenhæng mellem antallet af stjerner og pris
#Fortæller prisen om produktets kvalitet? 
#