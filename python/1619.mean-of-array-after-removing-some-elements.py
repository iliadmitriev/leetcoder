class Solution:
    def trimMean(self, arr: list[int]) -> float:

        n = len(arr)
        k = n * 5 // 100

        arr.sort()
        return sum(arr[k:-k]) / (n - 2 * k)

