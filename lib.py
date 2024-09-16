import pandas as pd
import matplotlib.pyplot as plt

# Data Preprocessing
def preprocess_data():
    stock = pd.read_csv("NASDAQ_100_Data_From_2010.csv", sep="\t")
    stock_AAPL = stock.loc[stock["Name"] == "AAPL"].copy()  # Only use AAPL stock data

    # Extract "Year" info from "Date" Column
    stock_AAPL.loc[:,'Date'] = pd.to_datetime(stock_AAPL.Date)
    stock_AAPL.set_index("Date", inplace=True)
    stock_AAPL.loc[:,"Year"] = stock_AAPL.index.year  # Add a new column 'Year'
    
    return stock_AAPL

# Plotting the statistics
def generate_plot(yearly_stats):
    plt.figure(figsize=(15, 6))
    plt.plot(yearly_stats.index, yearly_stats["mean"], label="Mean", marker="o")
    plt.plot(yearly_stats.index, yearly_stats["median"], label="Median", marker="x")
    plt.plot(
        yearly_stats.index, yearly_stats["std"], label="Standard Deviation", marker="s"
    )
    plt.grid(True)

    plt.title("AAPL Close Price Statistics (2010-2021)")
    plt.xlabel("Year")
    plt.ylabel("Price")
    plt.legend()
    plt.savefig("plot.png")
