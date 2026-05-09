class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        res = arr[0]
        count = 1
        for i in range(1, n):
            if arr[i - 1] == arr[i]:
                count += 1
            else:
                count = 1

            if count > n // 4:
                res = arr[i]
                break

        return res