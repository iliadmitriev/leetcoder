class Solution:
    def getLucky(self, s: str, k: int) -> int:

        nums = "".join(str(ord(ch) - ord("a") + 1) for ch in s)

        for _ in range(k):
            nums = str(sum(int(d) for d in nums))

        return int(nums)

