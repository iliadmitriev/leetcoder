def max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

    return arr


def heappop(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1:
        return arr.pop()
    arr[0], arr[n - 1] = arr[n - 1], arr[0]
    heapify(arr, n - 1, 0)
    return arr.pop()


def heappush(arr, val):
    arr.append(val)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = max_heap(stones)
        
        while len(hq) > 1:
            a = heappop(hq)
            b = heappop(hq)
            
            if a > b:
                heappush(hq, a - b)
        
        # in case all stones finished draw
        return hq[0] if hq else 0