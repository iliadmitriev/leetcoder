class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        today = 0

        for start, end in meetings:
            if today >= end:
                continue

            if start > today:
                days -= end - start + 1
            else:
                days -= end - today

            today = end

        return days

