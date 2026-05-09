
import datetime as dt


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        t = dt.datetime(year, month, day)

        return t.strftime("%A")

