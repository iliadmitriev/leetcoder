import datetime as dt


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = dt.datetime.strptime(date1, "%Y-%m-%d")
        d2 = dt.datetime.strptime(date2, "%Y-%m-%d")

        return abs((d1 - d2).days)

