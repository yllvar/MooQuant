# mooquant/utils.py
def validate_stock_code(stock_code, market):
    """Add market prefix if missing"""
    if market == "US" and not stock_code.startswith('US.'):
        return f'US.{stock_code}'
    elif market == "HK" and not stock_code.startswith('HK.'):
        return f'HK.{stock_code}'
    elif market == "CN" and not stock_code.startswith('SH.'):
        return f'SH.{stock_code}'
    return stock_code