class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        indices = sorted(range(len(growTime)), key=lambda x: growTime[x], reverse=True)
        bloom = 0
        total_plant = 0
        for i in indices:
            total_plant += plantTime[i]
            bloom = max(bloom, total_plant + growTime[i])
            
        return bloom