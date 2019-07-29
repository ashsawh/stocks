from typing import Optional


class Stock:
    """
    Contains data pertaining to a stock
    """
    symbol: Optional[str] = None
    amount: int = 0

    def __init__(self, symbol: str, amount: float):
        """
        Instantiate stock object

        :param symbol:
        :param amount:
        """
        self.symbol = symbol
        self.amount = amount


class BaseTransaction:
    """
    Base Transaction cass to pass down functionality
    """
    def __init__(self, symbol: str, amount: float, strike: float, transaction_type: str):
        """
        Instantiate a transaction

        :param symbol:
        :param amount:
        :param strike:
        :param transaction_type:
        """
        self.symbol = symbol
        self.amount = amount
        self.strike = strike
        self.type = transaction_type


class StockTransaction(BaseTransaction):
    """
    Stock transaction data
    """
    type: str = "BUY"

    def __init__(self, symbol: str, amount: float, strike: float, transaction_type: str = "BUY"):
        """
        Instantiate a stock transaction

        :param symbol:
        :param amount:
        :param strike:
        :param transaction_type:
        """
        if transaction_type != "BUY":
            self.type = "SELL"
            amount = -amount
        else:
            strike = -strike

        super().__init__(symbol, amount, strike, transaction_type)


class CashTransaction(BaseTransaction):
    """
    Contains cash transaction data
    """
    transaction_type: str = "DEPOSIT"

    def __init__(self, symbol: str, amount: float, strike: float, transaction_type: str = "DEPOSIT"):
        """
        Instantiate a cash transaction

        :param symbol:
        :param amount:
        :param strike:
        :param transaction_type:
        """
        if transaction_type not in ("DEPOSIT", "DIVIDEND"):
            self.type = transaction_type
            amount = -amount
            strike = -strike

        super().__init__(symbol, amount, strike, transaction_type)
