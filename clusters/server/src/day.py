from __future__ import annotations
from typing import List, Dict, Optional
from .value_objects import StockTransaction, BaseTransaction, CashTransaction, Stock


class Day:
    """
    Contains all logic that relates to daily stocks
    """
    def __init__(self, cash: int, designation: str):
        """
        Instantiate a day

        :param cash:
        :param designation:
        """
        self.cash: int = cash
        self.designation: str = designation
        self.catalog: List[str] = []
        self.stocks: List[Stock] = []
        self.transactions: Dict = {}
        self.cash_transactions: List[int] = []

    def set_catalog(self) -> Day:
        """
        Set stocks within a day

        :return:
        """
        self.catalog = set([stock.symbol for stock in self.stocks])
        return self

    def add(self, stock: Stock) -> Optional[Day]:
        """
        Add a stock to catalog and to day

        :param stock:
        :return:
        """
        if stock.symbol not in self.catalog:
            self.catalog.append(stock.symbol)
            self.stocks.append(stock)
            return self
        else:
            raise ValueError('Duplicated stock not allowed: ' + stock.symbol)

    def fill(self, stocks: List[Stock]) -> Day:
        """
        Fill a day with all stocks

        :param stocks:
        :return:
        """
        for stock in stocks:
            self.add(stock)
        return self

    def add_stock_transaction(self, stock: StockTransaction) -> Day:
        """
        Add a stock transaction

        :param stock:
        :return:
        """
        if stock.symbol in self.transactions:
            self.transactions[stock.symbol].append({"strike": stock.strike, "amount": stock.amount})
        else:
            self.transactions[stock.symbol] = [{"strike": stock.strike, "amount": stock.amount}]
        return self

    def add_cash_transaction(self, cash_transaction: CashTransaction) -> Day:
        """
        Add a cash transaction

        :param cash_transaction:
        :return:
        """
        self.cash_transactions.append(cash_transaction.strike)
        return self

    def get_closing_stocks(self) -> Dict:
        """
        Get stocks state at closing

        :return:
        """
        # create a dict of all cumulative transactions
        closing_values = {}

        for symbol, transactions in self.transactions.items():
            for transaction in transactions:
                if symbol in closing_values:
                    closing_values[symbol] += transaction["amount"]
                else:
                    closing_values[symbol] = transaction["amount"]

        final = {}
        stock_values = self.get_stocks()

        # loop through cumulative transaction value and add/subtract to start of the day portfolio
        for symbol, transaction in closing_values.items():
            if symbol in stock_values:
                if closing_values[symbol] + stock_values[symbol] != 0:
                    final[symbol] = closing_values[symbol] + stock_values[symbol]
            else:
                final[symbol] = closing_values[symbol]

        # add stocks that had no transactions for the day
        for symbol in self.catalog:
            if symbol not in closing_values:
                final[symbol] = stock_values[symbol]

        # returns a dict of days end value
        return final

    def get_closing_cash(self) -> int:
        """
        Get total cash at closing

        :return:
        """

        stocks_total = [transaction['strike']
            for symbol, trans_data in self.transactions.items()
                for transaction in trans_data
        ]

        return self.cash + sum(self.cash_transactions) + sum(stocks_total)

    def add_transactions(self, transactions: List[BaseTransaction]) -> Day:
        """
        Add all stock and cash transactions

        :param transactions:
        :return:
        """
        for transaction in transactions:
            if isinstance(transaction, CashTransaction):
                self.add_cash_transaction(transaction)
            else:
                self.add_stock_transaction(transaction)

        return self

    def get_stocks(self) -> Dict:
        """
        Get a dictionary of all stocks

        :return:
        """
        return {stock.symbol: stock.amount for stock in self.stocks}
