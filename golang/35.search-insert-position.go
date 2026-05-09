func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums)
    var mid int

    for left < right {
        mid = (right + left) / 2

        if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }

    return left
}