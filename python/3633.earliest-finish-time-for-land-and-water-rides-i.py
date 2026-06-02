class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        best_land = min(s + d for s, d in zip(landStartTime, landDuration))
        best_water = min(s + d for s, d in zip(waterStartTime, waterDuration))

        return min(
          min(max(s, best_water) + d for s, d in zip(landStartTime, landDuration)),
          min(max(s, best_land) + d for s, d in zip(waterStartTime, waterDuration)),
        )

         