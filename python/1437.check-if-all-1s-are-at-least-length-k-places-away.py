class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        distance = 0

        for num in nums:
            if num == 1:
                if distance > 0:
                    return False
                distance = k
            else:
                distance -= 1

        return True

