from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            if seats[i] > students[i]:
                res += seats[i] - students[i]
            else:
                res += students[i] - seats[i]

        return res

