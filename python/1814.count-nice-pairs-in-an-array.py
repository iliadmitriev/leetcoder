MOD = 10**9 + 7

def rev(x: int) -> int:
    y = 0
    while x > 0:
        x, rem = divmod(x, 10)
        y *= 10
        y += rem
    return y

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freq = Counter(map(lambda x: x - rev(x), nums))

        count = 0
        for _, v in freq.items():
            count += v * (v - 1) // 2

        return count % MOD