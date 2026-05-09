import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        n = len(classes)

        def extra(_pass: int, _total: int) -> float:
            x = (_pass + 1) / (_total + 1) - _pass / _total
            return -x

        hq = [
            (extra(_pass, _total), i)
            for i, (_pass, _total) in enumerate(classes)
            if _pass < _total
        ]
        heapq.heapify(hq)

        while extraStudents and hq:
            _, i = heapq.heappop(hq)

            classes[i][0] += 1
            classes[i][1] += 1

            heapq.heappush(hq, (extra(classes[i][0], classes[i][1]), i))

            extraStudents -= 1

        return sum(_pass / _total for _pass, _total in classes) / n

