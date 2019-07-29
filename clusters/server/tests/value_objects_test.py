import unittest
from src.value_objects import Stock, StockTransaction, CashTransaction


class ValueObjectTest(unittest.TestCase):
    def test_stock(self):
        aapl = Stock('AAPL', 20)
        self.assertEqual(aapl.symbol, 'AAPL')
        self.assertEqual(aapl.amount, 20)

    def test_stock_transaction(self):
        aapl = StockTransaction('AAPL', 20, 10000, 'BUY')
        self.assertEqual(aapl.symbol, 'AAPL')
        self.assertEqual(aapl.amount, 20)
        self.assertEqual(aapl.strike, -10000)
        self.assertEqual(aapl.type, "BUY")

    def test_cash_transaction(self):
        aapl = StockTransaction('CASH', 0, 10000, 'DEPOSIT')
        self.assertEqual(aapl.symbol, 'CASH')
        self.assertEqual(aapl.amount, 0)
        self.assertEqual(aapl.strike, 10000)
        self.assertEqual(aapl.type, "DEPOSIT")


if __name__ == '__main__':
    unittest.main()
