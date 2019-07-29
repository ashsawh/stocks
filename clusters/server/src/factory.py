from typing import List
from .value_objects import StockTransaction, CashTransaction, BaseTransaction, Stock
from .day import Day


class DayFactory:
    """
    Creates an instance of a day
    """
    @staticmethod
    def create(designation: str, stocks_input: List[str], cash: int = 0):
        """
        Create a day object

        :param designation:
        :param stocks_input:
        :param cash:
        :return:
        """
        day = Day(cash, designation)

        for stock in stocks_input:
            name, amt = stock.split(" ")
            day.add(Stock(name, float(amt)))

        return day


class TransactionsFactory:
    """
    Creates an instance of a transaction. Can be cash or stock
    """
    @staticmethod
    def create(input: List[str]) -> List[BaseTransaction]:
        """
        Create a stock or cash transaction

        :param input:
        :return:
        """
        transactions = []

        for transaction in input:
            name, transaction_type, amt, strike = transaction.split(" ")
            if name != "CASH" and transaction_type != "DIVIDEND":
                transactions.append(StockTransaction(name, float(amt), float(strike), transaction_type))
            else:
                transactions.append(CashTransaction(name, float(amt), float(strike), transaction_type))

        return transactions
