class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        hq: list[tuple[float, int, int]] = []

        for i in range(n - 1):
            heappush(hq, (arr[i] / arr[n - 1], i, n - 1))

        k -= 1
        while k:
            _, i, j = heappop(hq)

            if i < j - 1:
                heappush(hq, (arr[i] / arr[j - 1], i, j - 1))

            k -= 1

        _, i, j = heappop(hq)
        return [arr[i], arr[j]]

