class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mp = {}
        for num in nums2:
            while stack and stack[-1] < num:
                mp[stack.pop()] = num
            stack.append(num)

        return map(lambda x: mp.get(x, -1), nums1)