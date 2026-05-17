class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        vis = [False] * n

        def dfs(i: int) -> bool:
            if arr[i] == 0:
                return True

            if vis[i]:
                return False

            vis[i] = True

            if i - arr[i] >= 0 and dfs(i - arr[i]):
                return True

            return i + arr[i] < n and dfs(i + arr[i])

        return dfs(start)
