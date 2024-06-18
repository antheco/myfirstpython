from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests, numpy as np
#import the pandas library and aliasing as pd
import pandas as pd

##initiate arrays
##from array import *
a = []
b = []
newArray = []
tempArray = []

##set the website url
website = requests.get('https://finance.yahoo.com/quote/TSLA/history?p=TSLA')
soup = BeautifulSoup(website.content, 'html.parser')

##scrapes dates (1 dimension)
dates = soup.find_all(class_ = "Py(10px) Ta(start) Pend(10px)")
for soups in dates:
	##print(soups.string)
	a.append(soups.string)

##scrapes prices (6 columns)
	allPrices = soup.find_all(class_ = "Py(10px) Pstart(10px)")
for soups in allPrices:
	##print(soups.string)
	b.append(soups.string)

##print(b)

startint =0
endint = 0
i = 0
while i < len(a)-1:
	startint = i*6
	endint = (i*6)+6
	tempArray.append(a[i]) ##appends date to tempArray
	tempArray[2:2] = b[startint:endint] ##appends 6 fields of data to tempArray right after the date
	newArray.append(tempArray)
	tempArray = []
	##newArray.append(a[i+1])
	##newArray.append(b[startint:endint])
	i+=1

##print(newArray)
##newArray = np.array_split(b,6)
##print(newArray[5])

data = newArray
df = pd.DataFrame(data,columns=['date','open','high','low','close','adj close','vol'],dtype=float)
print (df)

# Create a Figure with one Axis on it
fig, ax = plt.subplots()

##fixing the size of the plot
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
##fig.savefig('test2png.png', dpi=100)

# The x-values of the bars.
date = df['date']
x = np.arange(len(date))

# The width of the bars (1 = the whole width of the 'date group')
width = 0.2

# Create the bar charts!
ax.bar(x - 3*width/2, df['open'], width, label='Open', color='#0343df')
ax.bar(x - width/2, df['high'], width, label='High', color='#e50000')
ax.plot(x, df['vol'], 'go--', linewidth=.5, markersize=2)

# Notice that features like labels and titles are added in separate steps
ax.set_ylabel('Price (USD)')
ax.set_title('TESLA (TSLA) Stock Prices')

ax.set_xticks(x)    # This ensures we have one tick per year, otherwise we get fewer
ax.set_xticklabels(date.astype(str).values, rotation='vertical')
plt.gca().invert_xaxis() ##inverts x-axis series

ax.plot(x, df['open'] - df['close'], label='Daily movement', color='black', linestyle='dashed')
ax.grid(color='#eeeeee')
ax.set_axisbelow(True)
ax.set_ylim([-40, 900])

ax.legend()
plt.show()