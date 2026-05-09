import heapq


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        score = 0

        def divide(x: int, y: int) -> int:
            if x % y != 0:
                return x // y + 1
            return x // y

        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        while k:
            top = -heapq.heappop(maxHeap)

            if top == 1:
                score += k
                k = 0
            else:
                score += top
                heapq.heappush(maxHeap, -divide(top, 3))
                k -= 1

        return score

