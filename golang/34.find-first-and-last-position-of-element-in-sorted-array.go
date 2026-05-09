func left(arr []int, target int) int {
    lo, hi := 0, len(arr)
    var mid int
    for lo < hi {
        mid = (lo + hi) / 2
        if arr[mid] < target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }

    if lo < len(arr) && arr[lo] == target {
        return lo
    }
    return -1
}

func right(arr []int, target int) int {
    lo, hi := 0, len(arr)
    var mid int
    for lo < hi {
        mid = (lo + hi) / 2
        if arr[mid] <= target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }

    if lo - 1 >= 0 && arr[lo - 1] == target {
        return lo - 1
    }
    return -1
}

func searchRange(nums []int, target int) []int {
    return []int{ left(nums, target), right(nums, target) }
}