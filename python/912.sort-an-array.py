

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def heapify(arr: list[int], start: int, end: int) -> None:
            parent = start
            child = 2 * parent + 1

            while child <= end:
                if child < end and arr[child] < arr[child + 1]:
                    child += 1

                if arr[parent] < arr[child]:
                    arr[parent], arr[child] = arr[child], arr[parent]
                    parent = child
                    child = 2 * parent + 1
                else:
                    break

        def heap_sort(arr: list[int]) -> list[int]:
            n = len(arr)

            for i in range(n - 1, -1, -1):
                heapify(arr, i, n - 1)

            for i in range(n - 1, 0, -1):
                arr[0], arr[i] = arr[i], arr[0]
                heapify(arr, 0, i - 1)
            return arr

        return heap_sort(nums)

