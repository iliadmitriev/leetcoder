from bisect import bisect


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if i < j < k and  nums[i] < nums[k] < nums[j]:
        #                 print(i,j, k)
        #                 print(nums[i], nums[k], nums[j])
        #                 return True
        st = []
        last = float("inf")
        for num in nums:

            while st and st[-1][0] < num:
                st.pop()

            if st and st[-1][0] > num and num > st[-1][1]:
                return True

            st.append((num, last))
            last = min(last, num)

        return False