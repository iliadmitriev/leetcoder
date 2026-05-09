class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        el1, el2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if cnt1 == 0 and el2 != num:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0 and el1 != num:
                el2 = num
                cnt2 = 1
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        if nums.count(el1) > len(nums) // 3:
            res.append(el1)

        if nums.count(el2) > len(nums) // 3:
            res.append(el2)
        
        return res
        