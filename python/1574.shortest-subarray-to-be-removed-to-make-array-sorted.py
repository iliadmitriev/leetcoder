class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        i, j = 0, n - 1

        while i < j and arr[i] <= arr[i + 1]:
            i += 1

        # all elements are sorted
        if i == n - 1:
            return 0

        while i < j and arr[j] >= arr[j - 1]:
            j -= 1

        minLen = min(j, n - i - 1)

        left = i
        i = 0

        while i <= left and j < n:
            if arr[i] <= arr[j]:
                minLen = min(minLen, j - i - 1)
                i += 1
            else:
                j += 1

        return minLen

