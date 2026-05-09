

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        days.sort()

        fare = list(zip([1, 7, 30], costs))
        lastDay = days[-1]
        dp = [0] * (lastDay + 1)

        j = 0
        for curDay in range(1, lastDay + 1):
            if curDay < days[j]:
                # current day is covered with payment
                dp[curDay] = dp[curDay - 1]
            else:
                j += 1
                dp[curDay] = min(dp[max(0, curDay - day)] + cost for day, cost in fare)

        print(dp)

        return dp[lastDay]

