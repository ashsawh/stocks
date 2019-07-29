import unittest
from src.factory import DayFactory, TransactionsFactory
from src.value_objects import Stock, StockTransaction, CashTransaction


class FactoryTest(unittest.TestCase):
    def test_create_day(self):
        """
        Assert factory method returns a dictionary

        :return:
        """
        D0 = DayFactory().create("D0", ["AAPL 100", "GOOG 200", "SP500 175.75"], 1000)

        self.assertEqual(D0.catalog, ["AAPL", "GOOG", "SP500"])
        self.assertEqual(D0.cash, 1000)
        stock = Stock('AAPL', 100)
        popped = D0.stocks.pop(0)
        self.assertEqual(popped.symbol, stock.symbol)
        self.assertEqual(popped.amount, stock.amount)

    def test_create_translation(self):
        T0 = TransactionsFactory().create([
            "AAPL SELL 100 30000",
            "GOOG BUY 10 10000",
            "CASH DEPOSIT 0 1000",
            "CASH FEE 0 50",
            "GOOG DIVIDEND 0 50",
            "TD BUY 100 10000"
        ])
        """
        Assert factory method returns list of dictionary

        :return:
        """
        self.assertEqual(T0[0].symbol, "AAPL")
        self.assertEqual(T0[0].amount, -100.0)
        self.assertEqual(T0[0].strike, 30000.0)
        self.assertEqual(T0[0].type, "SELL")


if __name__ == '__main__':
    unittest.main()
