class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = list(freq.values())
        heapq.heapify(heap)

        res = len(heap)

        while k > 0 and heap and heap[0] <= k:
            k -= heapq.heappop(heap)
            res -= 1

        return res