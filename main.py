# Dataset from https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data/data

import pandas as pd
import matplotlib.pyplot as plt

# Data Preprocessing
def preprocess_data():
    stock = pd.read_csv('NASDAQ_100_Data_From_2010.csv',sep='\t')
    stock_AAPL = stock.loc[stock['Name'] == 'AAPL']  # Only use AAPL stock data

    # Extract "Year" info from "Date" Column
    stock_AAPL.Date = pd.to_datetime(stock_AAPL.Date)
    stock_AAPL.set_index('Date', inplace=True)  
    stock_AAPL['Year'] = stock_AAPL.index.year  # Add a new column 'Year'

    # Sort by 'Year', use 'Close' to calculate its stock's mean, median, std data
    yearly_stats = stock_AAPL.groupby('Year')['Close'].agg(['mean', 'median', 'std'])
    return yearly_stats

# Plotting the statistics
def generate_plot(yearly_stats):
    plt.figure(figsize=(15, 6))
    plt.plot(yearly_stats.index, yearly_stats['mean'], label='Mean', marker='o')
    plt.plot(yearly_stats.index, yearly_stats['median'], label='Median', marker='x')
    plt.plot(yearly_stats.index, yearly_stats['std'], label='Standard Deviation', marker='s')
    plt.grid(True)

    plt.title('AAPL Close Price Statistics (2010-2021)')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig('plot.png')


if __name__ == '__main__':
    data = preprocess_data()
    generate_plot(data)