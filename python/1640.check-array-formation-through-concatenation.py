class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        # since all numbers in arr is distinct
        adj: dict[int, list[int]] = {}
        for p in pieces:
            adj[p[0]] = p

        if arr[0] not in adj:
            return False

        p = adj[arr[0]]
        i, j = 0, 0
        while i < len(arr):
            if j == len(p):
                if arr[i] not in adj:
                    return False

                p = adj[arr[i]]
                j = 0

            if arr[i] != p[j]:
                return False

            j += 1
            i += 1

        return True

