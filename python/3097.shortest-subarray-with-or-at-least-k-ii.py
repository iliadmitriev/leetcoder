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
            num = nums[right]

            cur |= num

            j = 0
            while num:
                bitCount[j] += num & 1
                j += 1
                num >>= 1

            while left <= right and cur >= k:
                minLen = min(minLen, right - left + 1)

                num = nums[left]
                j = 0
                while num:
                    bitCount[j] -= num & 1

                    if bitCount[j] == 0 and (cur >> j) & 1:
                        cur ^= 1 << j

                    j += 1
                    num >>= 1

                left += 1

        if minLen > n:
            return -1

        return minLen

