from .day import Day
from typing import Dict


class Recon:
    """
    Recon primarily returns differences in day 1 end to day 2 start that were somehow missed by transaction log
    """
    @staticmethod
    def compare(first_day: Day, second_day: Day) -> Dict:
        """
        Compare two days to get differences

        :param first_day:
        :param second_day:
        :return:
        """
        differences = {}
        first_day_end = first_day.get_closing_stocks()
        first_day_stocks = [symbol for symbol, amount in first_day_end.items()]
        second_day_start = second_day.get_stocks()

        # get difference of all second day - first day. If stock matches in value don't return
        for symbol, amount in second_day_start.items():
            if symbol not in first_day_stocks:
                differences[symbol] = amount
            else:
                diff = amount - first_day_end[symbol]
                if diff != 0:
                    differences[symbol] = diff

        # if a stock shows in in day  1 but not day 2, return day 1 amount as negative
        for symbol in first_day_stocks:
            if symbol not in second_day_start:
                differences[symbol] = -first_day_end[symbol]

        # calculate cash difference from day 2 to day 1
        differences["Cash"] = second_day.cash - first_day.get_closing_cash()

        # returns a dict containing symbol to difference amounts
        return differences

