# examples/basic_usage.py
from mooquant.connection import MooMooConnection
from mooquant.market_data import MarketData
from mooquant.trading import Trading

def main():
    # Initialize connection
    conn = MooMooConnection()
    
    try:
        # Connect to MooMoo
        conn.connect()
        
        # Initialize modules
        market = MarketData(conn)
        trading = Trading(conn)
        
        # Example usage
        print("AAPL Market Data:", market.get_real_time_quote("AAPL"))
        print("Account Info:", trading.get_account_info())
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.disconnect()

if __name__ == "__main__":
    main()