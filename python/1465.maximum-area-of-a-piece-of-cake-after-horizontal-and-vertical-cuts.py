class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hor = sorted([0] + horizontalCuts + [h])
        ver = sorted([0] + verticalCuts + [w])
        hor_max = max(map(operator.sub, hor[1:], hor[:-1]))
        ver_max = max(map(operator.sub, ver[1:], ver[:-1]))
        return (hor_max * ver_max) % (10**9 + 7)