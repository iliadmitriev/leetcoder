class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:

        N = 101
        set1, set2, set3 = [0] * N, [0] * N, [0] * N

        for num in nums1:
            set1[num] = 1

        for num in nums2:
            set2[num] = 1

        for num in nums3:
            set3[num] = 1

        res: list[int] = []
        for i in range(1, 101):
            if set1[i] + set2[i] + set3[i] > 1:
                res.append(i)

        return res

