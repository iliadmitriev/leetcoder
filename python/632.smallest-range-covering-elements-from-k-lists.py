import heapq


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:

        n = len(nums)
        ind = [0] * n  # indices of elements in each list

        minHeap: list[tuple[int, int]] = []

        right = nums[0][0]
        for i, arr in enumerate(nums):
            heapq.heappush(minHeap, (arr[ind[i]], i))
            right = max(right, arr[ind[i]])
            ind[i] += 1

        minDiff = right - minHeap[0][0]
        res = [minHeap[0][0], right]

        while minHeap:
            left, i = heapq.heappop(minHeap)

            if right - left < minDiff:
                minDiff = right - left
                res = [left, right]

            if ind[i] == len(nums[i]):
                break

            heapq.heappush(minHeap, (nums[i][ind[i]], i))
            right = max(right, nums[i][ind[i]])

            ind[i] += 1

        return res

