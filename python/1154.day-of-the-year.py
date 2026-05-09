import datetime as dt


class Solution:
    def dayOfYear(self, date: str) -> int:
        t = dt.datetime.strptime(date, "%Y-%m-%d")  # beginning of the day
        t_ = dt.datetime(t.year, 1, 1)  # beginning of the year

        s = int(t.timestamp() - t_.timestamp())  # difference in seconds
        return s // 86400 + 1  # number of days starting from 1

