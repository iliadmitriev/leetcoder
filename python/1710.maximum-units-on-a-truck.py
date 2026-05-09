from operator import itemgetter

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res_units = 0
        for boxes, units in sorted(boxTypes, key=itemgetter(1), reverse=True):
            left_boxes = min(truckSize, boxes)
            res_units += left_boxes * units
            truckSize -= left_boxes
            if truckSize == 0:
                break
        return res_units