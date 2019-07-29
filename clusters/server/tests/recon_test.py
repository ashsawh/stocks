import unittest
from src.factory import DayFactory, TransactionsFactory
from src.day import Day
from src.recon import Recon


class ReconTest(unittest.TestCase):
    def setUp(self):
        self.D0: Day = DayFactory().create("D0", ["AAPL 100", "GOOG 200", "SP500 175.75"], 1000)
        self.D1: Day = DayFactory().create("D0", ["AAPL 120", "GOOG 220", "SP500 175.75"], 10000)

        self.stock_list = ["AAPL", "GOOG", "SP500"]
        self.r = Recon()

    def test_compare(self):
        self.assertEqual(self.r.compare(self.D0, self.D1), {'AAPL': 20.0, 'GOOG': 20.0, 'Cash': 9000})


if __name__ == '__main__':
    unittest.main()
