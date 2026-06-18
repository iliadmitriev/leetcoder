class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hours_full = 12
        minutes_full = 60
        circle_full = 360

        # number of degrees in hour (30.0)
        one_hour = circle_full / hours_full
        # number of degrees in minute (6.0)
        one_minute = circle_full / minutes_full
        # number of gegrees in a hour's minute (0.5)
        one_hour_minute = circle_full / hours_full / minutes_full

        hour %= hours_full  # 12 -> 0

        minute_angle = minutes * one_minute
        hour_angle = hour * one_hour + minutes * one_hour_minute

        angle = abs(minute_angle - hour_angle)

        return min(angle, circle_full - angle)
