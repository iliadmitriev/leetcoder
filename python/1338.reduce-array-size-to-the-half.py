class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        goal = len(arr) // 2
        
        res = 0
        ans = 0
        for val in sorted(count.values(), reverse=True):
            res += val
            ans += 1
            if res >= goal:
                break
        
        return ans