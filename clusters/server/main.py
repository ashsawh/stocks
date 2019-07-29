from src.recon import Day
from src.factory import DayFactory, TransactionsFactory
from src.recon import Recon

if __name__ == '__main__':
    # create the days and add transactions
    D0: Day = DayFactory().create("D0", ["AAPL 100", "GOOG 200",  "SP500 175.75"], 1000)
    D1: Day = DayFactory().create("D1", ["MSFT 10", "GOOG 220",  "SP500 175.75"], 20000)

    T0 = TransactionsFactory().create([
        "AAPL SELL 100 30000",
        "GOOG BUY 10 10000",
        "CASH DEPOSIT 0 1000",
        "CASH FEE 0 50",
        "GOOG DIVIDEND 0 50",
        "TD BUY 100 10000"
    ])

    D0.add_transactions(T0)

    # compare the two days
    r = Recon()
    print("recon.out\r\n", "--------\r\n", r.compare(D0, D1))
