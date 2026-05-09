import heapq


class Solution:
    def findScore(self, nums: list[int]) -> int:
        score = 0
        marked = set()
        hq = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(hq)

        while hq:
            top, index = heapq.heappop(hq)

            if index in marked:
                continue

            score += top
            marked.add(index)
            marked.add(index + 1)
            marked.add(index - 1)

        return score

