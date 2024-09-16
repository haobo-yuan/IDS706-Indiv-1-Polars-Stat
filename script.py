from lib import preprocess_data, generate_plot

def main():
    # Load and preprocess data
    stock_AAPL = preprocess_data()
    print(stock_AAPL)

    # Descriptive Statistics
    yearly_stats = stock_AAPL.groupby("Year")["Close"].agg(["mean", "median", "std"])
    print(yearly_stats)

    # Visualization
    generate_plot(yearly_stats)

if __name__ == "__main__":
    main()
