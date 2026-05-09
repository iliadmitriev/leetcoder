class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)

        i = n - 1

        while i >= 0 and zeros > 0:
            if i + zeros < n:
                arr[i + zeros] = arr[i]

            if arr[i] == 0:
                zeros -= 1

                if i + zeros < n:
                    arr[i + zeros] = 0

            i -= 1

