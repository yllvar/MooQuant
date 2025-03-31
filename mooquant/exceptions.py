# mooquant/exceptions.py
class MooQuantError(Exception):
    """Base exception class"""
    pass

class MooQuantConnectionError(MooQuantError):
    """Connection related errors"""
    pass

class MooQuantDataError(MooQuantError):
    """Market data related errors"""
    pass

class MooQuantTradingError(MooQuantError):
    """Trading related errors"""
    pass