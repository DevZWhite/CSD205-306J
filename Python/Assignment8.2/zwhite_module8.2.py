# Name: Zachary White
# Instructor: Darrell Payne
# Date: feb 25, 2026
# Assignment: Stock Dictionary Lookup Program

# Purpose:
# This program creates a dictionary containing at least
# ten stock ticker symbols and their current prices
# (fictional values). The program prompts the user to
# enter a ticker symbol, searches the dictionary for
# that symbol, and displays the ticker symbol along
# with its stock price if found. If the ticker symbol
# is not found, the program informs the user.

# Logic:
# 1. Create a dictionary containing at least 10 stock ticker symbols
#    as keys and fictional stock prices as values.
# 2. Prompt the user to enter a ticker symbol.
# 3. Convert the user's input to uppercase to ensure consistency.
# 4. Check if the ticker symbol exists in the dictionary.
# 5. If found, display the ticker symbol and its price.
# 6. If not found, display a message indicating it was not located.
# 7. Allow the user to continue searching until they choose to quit.


# Dictionary containing stock ticker symbols and fictional prices
stocks = {
    "AAPL": 189.45,
    "MSFT": 402.33,
    "GOOGL": 142.76,
    "AMZN": 178.90,
    "TSLA": 215.67,
    "META": 310.25,
    "NVDA": 721.84,
    "NFLX": 598.12,
    "INTC": 43.56,
    "AMD": 167.42
}


# Main function that drives the program
def main():
    # Keep looping until the user chooses to quit
    while True:
        # Prompt the user to enter a ticker symbol
        user_input = input("\nEnter a stock ticker symbol (or type 'quit' to exit): ").strip()

        # Allow the user to exit the program
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Convert input to uppercase for dictionary matching
        ticker = user_input.upper()

        # Check if the ticker symbol exists in the dictionary
        if ticker in stocks:
            # Retrieve the stock price from the dictionary
            price = stocks[ticker]

            # Display the ticker symbol and its price
            print(f"Ticker Symbol: {ticker}")
            print(f"Current Stock Price: ${price:.2f}")
        else:
            # Inform the user the ticker symbol was not found
            print(f"Ticker symbol '{ticker}' was not found in the dictionary.")


# Entry point — only run main() if this script is executed directly
if __name__ == "__main__":
    main()