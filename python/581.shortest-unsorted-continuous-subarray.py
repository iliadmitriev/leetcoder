class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # init left and right indexes vice-versa
        l, r = len(nums), 0
        
        stack = []
        
        # forward scan
        for i in range(len(nums)):
            
            # pop from stack if next element is not in ascending order
            # while correct position of element is not found or stack is not empty
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            
            # put index to stack
            stack.append(i)
            
        stack.clear()
        # backward scan
        for i in range(len(nums) - 1, -1, -1):
            
            # pop from stack if next element is not in descending order
            # while correct position of element is not found or stack is not empty 
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
                
            # put index to stack
            stack.append(i)
            
        print(l, r)
            
        return r - l + 1 if r - l > 0 else 0