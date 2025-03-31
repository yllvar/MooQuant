# mooquant/market_data.py
from moomoo.common import RET_OK
from .exceptions import MooQuantDataError
from .utils import validate_stock_code

class MarketData:
    def __init__(self, connection):
        self.conn = connection

    def get_market_state(self, stock_code):
        """Get market state for given stock"""
        validated_code = validate_stock_code(stock_code, self.conn.config["market"])
        ret, data = self.conn.quote_ctx.get_market_state([validated_code])
        if ret != RET_OK:
            raise MooQuantDataError(f"Failed to get market state: {data}")
        return data

    def get_real_time_quote(self, stock_code):
        """Get real-time quote data"""
        validated_code = validate_stock_code(stock_code, self.conn.config["market"])
        ret, data = self.conn.quote_ctx.get_stock_quote([validated_code])
        if ret != RET_OK:
            raise MooQuantDataError(f"Failed to get quote: {data}")
        return {
            'symbol': stock_code,
            'last_price': data['last_price'][0],
            'open': data['open_price'][0],
            'high': data['high_price'][0],
            'low': data['low_price'][0],
            'volume': data['volume'][0]
        }

    def get_historical_data(self, stock_code, start_date, end_date, ktype='K_DAY'):
        """Get historical kline data"""
        validated_code = validate_stock_code(stock_code, self.conn.config["market"])
        ret, data = self.conn.quote_ctx.get_history_kline(
            code=validated_code,
            start=start_date,
            end=end_date,
            ktype=ktype
        )
        if ret != RET_OK:
            raise MooQuantDataError(f"Failed to get historical data: {data}")
        return data