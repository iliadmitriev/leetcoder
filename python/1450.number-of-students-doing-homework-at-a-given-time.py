class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:

        return sum(a <= queryTime <= b for a, b in zip(startTime, endTime))

