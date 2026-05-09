func findPeakElement(nums []int) int {
    lo, hi := 0, len(nums) - 1

    var mid int;
    for lo < hi {
        mid = (lo + hi) / 2

        if nums[mid] > nums[mid + 1] {
            hi = mid
        } else {
            lo = mid + 1
        }
    }

    return lo
}