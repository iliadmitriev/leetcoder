"""

n - number of elements in the array
M - mininum element in the array (at start)
S - sum of all the elements at the start
k - number of moves to make elements equal

move| min | sum
----+-----+-----
 0  |  M  | S
 1  | M+1 | S + (n - 1)
... | ... | ...
 k  | M+k | S + k * (n - 1)


This yields:
(M + k) * n = S + k * (n - 1)
M * n + k * n = S + k * n - k
M * n = S - k
k = S - M * n
"""

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)