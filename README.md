# MooQuant - Quantitative Trading with MooMoo

MooQuant is a Python framework for algorithmic trading using MooMoo's OpenD API. It provides real-time market data, order execution, and account management capabilities in a modular and scalable design.

## 🚀 Features
- **Real-time Market Data**: Fetch live stock quotes, market state, and price movements.
- **Trading Execution**: Place market and limit orders programmatically.
- **Paper/Live Trading**: Support for simulated and real trading environments.
- **Account Management**: Retrieve cash balance, portfolio details, and order history.
- **Modular Architecture**: Designed for scalability and ease of use.
- **Error Handling & Logging**: Provides detailed logs for debugging and reliability.

## 📦 Installation

Before installing, ensure you have Python 3.7+ installed on your system.

```bash
pip install -r requirements.txt
```

## 🛠 Configuration
Set up your `config.py` file with your MooMoo OpenD API connection details:

```python
# config.py
HOST = "127.0.0.1"
PORT = 11112
TRADING_PASSWORD = "YOUR_TRADING_PASSWORD"
TRADING_ENV = "SIMULATE"  # Use "REAL" for live trading
MARKET = "US"
SECURITY_FIRM = "FUTUINC"
```

## 📂 Project Structure
```
MooQuant/
│── mooquant/
│   ├── __init__.py
│   ├── config.py             # Configuration settings
│   ├── connection.py         # API connection handler
│   ├── market_data.py        # Fetches market data
│   ├── trading.py            # Order execution and account management
│   ├── utils.py              # Helper functions
│── examples/
│   ├── basic_usage.py        # Example usage script
│── tests/
│   ├── test_connection.py    # Unit tests for connection
│   ├── test_market_data.py   # Unit tests for market data
│   ├── test_trading.py       # Unit tests for trading functions
│── .gitignore
│── README.md
│── requirements.txt
│── setup.py                  # Packaging setup
```

## 🏦 Usage

### 1️⃣ **Establish Connection**
```python
from mooquant.connection import MooMooConnection
conn = MooMooConnection()
conn.connect()
```

### 2️⃣ **Retrieve Market Data**
```python
from mooquant.market_data import MarketData
market_data = MarketData(conn)
market_data.get_real_time_quote("AAPL")
market_data.get_market_state("AAPL")
```

### 3️⃣ **Account Information**
```python
from mooquant.trading import Trading
trading = Trading(conn)
trading.get_account_info()
```

### 4️⃣ **Place an Order**
```python
# Place a market order (buy 1 share of AAPL)
trading.place_market_order("AAPL", 1, "BUY")
```

### 5️⃣ **Disconnect**
```python
conn.disconnect()
```

## 🔍 Example Script
An example script demonstrating the complete workflow is available in `examples/basic_usage.py`.

## ✅ Running Tests
Run unit tests to verify the functionality:
```bash
pytest tests/
```

## 🤝 Contributions
Contributions are welcome! Please open an issue or submit a pull request.

## 🛡 License
This project is licensed under the MIT License.

## 📬 Support
For any issues, open a GitHub issue or reach out to the MooMoo API support team.

