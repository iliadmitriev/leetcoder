class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        frequencies = Counter(nums)
        # dict to store subsequncies ends count
        # 1,2,3; 5,6,7; 2,3,4 -> {3: 1, 4: 1, 7: 1}
        subsequencies = defaultdict(int)
        
        for num in nums:
            
            if frequencies[num] == 0:
                continue
            
            # use number for continuing or starting a new conscutive subsequence
            frequencies[num] -= 1
            
            # continue subsequence
            if subsequencies[num - 1] > 0:
                # shift forward the end of subsequence
                subsequencies[num - 1] -= 1
                subsequencies[num] += 1
            
            # start a new subsequence if there is extra two consequtive elements
            elif frequencies[num + 1] and frequencies[num + 2]:
                # consume extra two elements
                frequencies[num + 1] -= 1
                frequencies[num + 2] -= 1
                subsequencies[num + 2] += 1
            
            # otherwise
            else:
                return False
            
        return True