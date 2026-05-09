class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 1

        n = len(nums)
        maxBits = (max(max(nums), k)).bit_length()

        bitCount = [0] * maxBits
        cur = 0
        minLen = n + 1
        left = 0

        for right in range(n):
            for j in range(maxBits):
                if (nums[right] >> j) & 1:
                    bitCount[j] += 1
                    cur |= 1 << j

            while left < n and cur >= k:
                minLen = min(minLen, right - left + 1)

                for j in range(maxBits):
                    if (nums[left] >> j) & 1:
                        bitCount[j] -= 1

                    if bitCount[j] == 0 and (cur >> j) & 1:
                        cur ^= 1 << j

                left += 1

        if minLen > n:
            return -1

        return minLen
