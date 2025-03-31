# mooquant/connection.py
from moomoo import OpenQuoteContext, OpenSecTradeContext
from moomoo.common import RET_OK, TrdEnv, TrdMarket
from .config import DEFAULT_CONFIG
from .exceptions import MooQuantConnectionError

class MooMooConnection:
    def __init__(self, config=None):
        self.config = config or DEFAULT_CONFIG
        self.quote_ctx = None
        self.trade_ctx = None
        self._connected = False

    def connect(self):
        """Establish connection to MooMoo OpenD"""
        try:
            # Initialize contexts
            self.quote_ctx = OpenQuoteContext(
                host=self.config["host"],
                port=self.config["port"]
            )
            
            self.trade_ctx = OpenSecTradeContext(
                host=self.config["host"],
                port=self.config["port"],
                security_firm=self.config["security_firm"],
                filter_trdmarket=TrdMarket[self.config["market"].value]
            )
            
            # Unlock trading if in real environment
            if self.config["env"] == Environment.REAL:
                ret, data = self.trade_ctx.unlock_trade(self.config["trading_password"])
                if ret != RET_OK:
                    raise MooQuantConnectionError(f"Failed to unlock trading: {data}")
            
            self._connected = True
            return True
            
        except Exception as e:
            raise MooQuantConnectionError(f"Connection failed: {str(e)}")

    @property
    def is_connected(self):
        return self._connected

    def disconnect(self):
        """Close all connections"""
        if self.quote_ctx:
            self.quote_ctx.close()
        if self.trade_ctx:
            self.trade_ctx.close()
        self._connected = False