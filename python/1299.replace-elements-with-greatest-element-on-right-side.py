class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        n = len(arr)
        maxRight = -1

        for i in range(n - 1, -1, -1):
            tmp = arr[i]
            arr[i] = maxRight
            if tmp > maxRight:
                maxRight = tmp

        return arr

