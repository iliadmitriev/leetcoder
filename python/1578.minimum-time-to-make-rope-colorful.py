class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i, j = 0, 0

        while i < len(neededTime) and j < len(neededTime):
            
            cur_total = 0
            cur_max = 0

            # calc while sum of repeating colors, and find max needed time of them
            while j < len(neededTime) and colors[i] == colors[j]:
                cur_total += neededTime[j]
                cur_max = max(cur_max, neededTime[j])
                j += 1
            
            # add to result all the time of repeating ballons 
            # but leave baloon with max time (minus max)
            total += cur_total - cur_max
            i = j

        return total