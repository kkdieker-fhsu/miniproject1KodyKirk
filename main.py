# INF601 - Advanced Programming in Python
# Kody Kirk
# Mini Project 1

# This project will be using the packages NumPy and Matplotlib in order to create 5 graphs that output as PNG files.
#
#     (5/5 points) Initial comments with your name, class and project at the top of your .py file.
#     (5/5 points) Proper import of packages used.
#     (20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#     (10/10 points) Store this information in a list that you will convert to a array in NumPy.
#     (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
#     (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#     (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#     (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#     (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

#import modules
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import yfinance as yf
import os

#pick stocks and make empty lists for the data
mystocks = ['MSFT', 'AAPL', 'NVDA', 'GOOG', 'TSLA']
stockdata = []
names = []

#for each stock in the above list, get its 10 day history, the closing prices on those days, the company's display name, and add all that to the empty lists
for i in mystocks:
    ticker = yf.Ticker(i)
    last10 = ticker.history(period='10d')
    closingprice = last10['Close'].tolist()
    names.append(ticker.info['displayName'])
    stockdata.append(closingprice)

#make a list of the dates themselves for plotting and convert the closing prices to a numpy array
closingdates = last10.index.tolist()
stockdata = np.array(stockdata, dtype=float)

#check if a folder titled 'charts' exists in the file location. if not, make one
if not os.path.exists('charts'):
    os.mkdir('charts')

#set the format for the dates on the plot to MM-DD to reduce clutter
format = mdates.DateFormatter('%m-%d')

#plotting; create and index variable that will be used to get the correct name from the names list
index = 0
for j in stockdata:
    #create the plot and set ticks and axis labels
    fig, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_xticks(ticks=closingdates)
    ax.tick_params(axis='x', labelrotation=45)
    ax.set_ylabel('Closing Price')
    ax.set_title(f'{names[index]} 10 Day Stock History')

    #plot the dates on the x axis and the closing prices on the y
    ax.plot(closingdates,j.round(decimals=2),marker='v',linestyle='--',color='r')

    #set the date format using the above
    ax.xaxis.set_major_formatter(format)

    #ensure that the axis labels remain visible
    fig.tight_layout()

    #save the plots
    fig.savefig(f'charts/{names[index]}.png', dpi=800)

    #clear the figure for the next one and iterate the index
    fig.clf()
    index += 1
