class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = sys.maxsize
        arr.sort()

        for i in range(len(arr) - 1):
            if min_diff > arr[i + 1] - arr[i]:
                min_diff = arr[i + 1] - arr[i]

        res = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                res.append([arr[i], arr[i + 1]])
                
        return res