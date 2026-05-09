

class MyCalendar:

    def __init__(self):
        self.__indexes: list[int] = []

    @staticmethod
    def search_rightmost(arr: list[int], target: int) -> int:
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        return lo

    @staticmethod
    def search_leftmost(arr: list[int], target: int) -> int:
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def book(self, start: int, end: int) -> bool:
        # find indexes
        # use rightmost index for start and leftmost for end
        # to prevent overlapping of two
        # intervals starting and ending with the same time
        # [1, 10) and [10, 14)
        start_idx = self.search_rightmost(self.__indexes, start)
        end_idx = self.search_leftmost(self.__indexes, end)

        # indexes should match and don't overlap with other interval
        if start_idx == end_idx and start_idx % 2 == 0:
            self.__indexes.insert(start_idx, end)
            self.__indexes.insert(start_idx, start)
            return True

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)