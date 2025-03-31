# mooquant/config.py
from enum import Enum

class Environment(Enum):
    SIMULATE = "SIMULATE"
    REAL = "REAL"

class Market(Enum):
    US = "US"
    HK = "HK"
    CN = "CN"

# Default configuration
DEFAULT_CONFIG = {
    "host": "127.0.0.1",
    "port": 11112,
    "trading_password": "YOUR_TRADING_PASSWORD",
    "env": Environment.SIMULATE,
    "market": Market.US,
    "security_firm": "FUTUINC"
}