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
    return lo
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
    return lo
}

func targetIndices(nums []int, target int) []int {
    sort.Ints(nums)
    lo, hi := left(nums, target), right(nums, target)
    res := make([]int, 0, 2)
    for i := lo; i < hi; i++ {
        res = append(res, i)
    }
    return res
}