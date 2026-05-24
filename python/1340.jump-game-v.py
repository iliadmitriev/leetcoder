class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        m = len(arr)
        seen = [-1] * m

        def dfs(pos: int) -> int:
            if seen[pos] != -1:
                return

            seen[pos] = 1

            # left
            i = pos - 1
            while i >= 0 and pos - i <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i -= 1

            # right
            i = pos + 1
            while i < m and i - pos <= d and arr[pos] > arr[i]:
                dfs(i)
                seen[pos] = max(seen[pos], seen[i] + 1)
                i += 1


        for i in range(m):
            dfs(i)

        return max(seen)



        