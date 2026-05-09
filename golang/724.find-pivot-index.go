func pivotIndex(nums []int) int {
    left, right := 0, 0
    for i := 1; i < len(nums); i++ { right += nums[i] }

    if left == right {
        return 0
    }

    for i := 1; i < len(nums); i++ {
        left += nums[i - 1]
        right -= nums[i]
        if left == right {
            return i
        }
    }

    return -1
}