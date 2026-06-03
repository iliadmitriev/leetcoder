class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        best_land = min(s + e for s, e in zip(landStartTime, landDuration))
        best_water = min(s + e for s, e in zip(waterStartTime, waterDuration))

        best_land_water = min(max(best_land, s) + e for s, e in zip(waterStartTime, waterDuration))
        best_water_land = min(max(best_water, s) + e for s, e in zip(landStartTime, landDuration))

        return min(best_land_water, best_water_land)
        