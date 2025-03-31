# mooquant/trading.py
from moomoo import TrdSide, OrderType, TrdEnv
from moomoo.common import RET_OK
from .exceptions import MooQuantTradingError
from .utils import validate_stock_code

class Trading:
    def __init__(self, connection):
        self.conn = connection

    def get_account_info(self):
        """Retrieve account information"""
        ret, data = self.conn.trade_ctx.accinfo_query(trd_env=TrdEnv[self.conn.config["env"].value])
        if ret != RET_OK:
            raise MooQuantTradingError(f"Failed to get account info: {data}")
        return {
            'cash': data['cash'][0],
            'total_assets': data['total_assets'][0],
            'market_value': data['market_val'][0]
        }

    def place_market_order(self, stock_code, quantity, side='BUY'):
        """Place market order"""
        validated_code = validate_stock_code(stock_code, self.conn.config["market"])
        trd_side = TrdSide.BUY if side.upper() == 'BUY' else TrdSide.SELL
        
        ret, data = self.conn.trade_ctx.place_order(
            price=0,  # Market order
            qty=quantity,
            code=validated_code,
            trd_side=trd_side,
            order_type=OrderType.MARKET,
            trd_env=TrdEnv[self.conn.config["env"].value]
        )
        
        if ret != RET_OK:
            raise MooQuantTradingError(f"Order failed: {data}")
        return data

    def get_order_list(self):
        """Retrieve current orders"""
        ret, data = self.conn.trade_ctx.order_list_query(trd_env=TrdEnv[self.conn.config["env"].value])
        if ret != RET_OK:
            raise MooQuantTradingError(f"Failed to get orders: {data}")
        return data