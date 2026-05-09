import datetime as dt


class Solution:
    def reformatDate(self, date: str) -> str:
        j = 0
        while date[j].isdigit():
            j += 1

        num = date[j : j + 2]

        d = dt.datetime.strptime(date, f"%d{num} %b %Y")

        return d.strftime("%Y-%m-%d")

