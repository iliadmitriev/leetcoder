func getAverages(nums []int, k int) []int {
    res := make([]int, len(nums))
    for i := range res { res[i] = -1 }

    // opt: return list of -1 without calculating window 
    // if window size greater than length of array
    if len(nums) <= 2 * k {
        return res
    }

    window := 0
    for i := 0; i < len(nums) && i < 2 * k; i++ {
        window += nums[i]
    }

    for i := k; i < len(nums) - k; i++ {
        window += nums[i + k]
        res[i] = window / (2 * k + 1)
        window -= nums[i - k]
    }

    return res
}