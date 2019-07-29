import unittest
from src.factory import DayFactory, TransactionsFactory
from src.value_objects import Stock, StockTransaction, CashTransaction
from src.day import Day


class DayTest(unittest.TestCase):
    def setUp(self):
        self.D0: Day = DayFactory().create("D0", ["AAPL 100", "GOOG 200", "SP500 175.75"], 1000)

        self.T0 = TransactionsFactory().create([
            "AAPL SELL 100 30000",
            "GOOG BUY 10 10000",
            "CASH DEPOSIT 0 1000",
            "CASH FEE 0 50",
            "GOOG DIVIDEND 0 50",
            "TD BUY 100 10000"
        ])

        self.stock_list = ["AAPL", "GOOG", "SP500"]

    def test_set_catalog(self):
        self.assertEqual(self.stock_list, self.D0.catalog)

    def test_get_stocks(self):
        self.assertEqual({"AAPL": 100, "GOOG": 200, "SP500": 175.75}, self.D0.get_stocks())

    def test_add(self):
        stock = Stock("MSFT", 100)
        self.D0.add(stock)
        self.assertEqual(self.D0.stocks[3], stock)

    def test_fill(self):
        facebook = Stock("F", 100)
        uber = Stock("Uber", 100)
        stocks = [facebook, uber]
        length = len(self.D0.stocks)
        self.D0.fill(stocks)
        self.assertEqual(self.D0.stocks[length].symbol, facebook.symbol)

    def test_add_stock_transaction(self):
        self.D0.add_stock_transaction(self.T0[0])
        self.assertEqual(self.D0.transactions["AAPL"][0]['amount'],  -100)

    def test_add_cash_transaction(self):
        transaction = CashTransaction("CASH", "0", 1000, "DEPOSIT")
        self.D0.add_cash_transaction(transaction)
        self.assertEqual(self.D0.cash_transactions[0], 1000)

    def test_add_transactions(self):
        self.D0.transactions = []
        self.D0.cash_transactions = []

    def test_get_closing_stocks(self):
        self.assertEqual({'AAPL': 100.0, 'GOOG': 200.0, 'SP500': 175.75}, self.D0.get_closing_stocks())

    def test_get_closing_cash(self):
        self.assertEqual(self.D0.get_closing_cash(), 1000)


if __name__ == '__main__':
    unittest.main()
