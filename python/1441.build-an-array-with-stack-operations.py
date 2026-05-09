class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        cur = 0
        
        for i in range(1, n + 1):
            if cur == len(target):
                break
            
            stack.append("Push")

            if target[cur] == i:
                cur += 1
            else:
                stack.append("Pop")
        
        return stack
