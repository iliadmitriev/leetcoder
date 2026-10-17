class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def sum_digits(x: int) -> int:
            y = 0
            while x:
                x, r = divmod(x, 10)
                y += r
            return y

        n = len(nums)

        arr = [(sum_digits(x), x, i) for i, x in enumerate(nums)]
        arr.sort()

        visited = [False] * n
        swaps = 0

        for i in range(n):
            # if already is visited or in the correct place
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            curr = i

            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1

            swaps += (cycle_size - 1)

        return swaps

            