from collections import Counter


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:

        freq = Counter((x % k + k) % k for x in arr)

        if freq[0] % 2 == 1:
            return False

        if k % 2 == 0 and freq[k // 2] % 2 == 1:
            return False

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        return True

