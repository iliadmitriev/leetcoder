from collections import Counter
from math import ceil


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()

        count = 0
        answer = 0
        for i in range(len(tasks)):
            count += 1
            if i == len(tasks) - 1 or tasks[i] != tasks[i + 1]:
                if count == 1:
                    return -1

                answer += ceil(count / 3)

                count = 0

        return answer
