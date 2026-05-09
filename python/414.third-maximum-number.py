class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        INF = -(1 << 32)
        A, B, C = INF, INF, INF

        for n in nums:
            if n > A:
                A, B, C = n, A, B
            elif n > B and n != A:
                B, C = n, B
            elif n > C and n != A and n != B:
                C = n

        if C == INF:
            C == B

        if C == INF:
            C = A

        return C

