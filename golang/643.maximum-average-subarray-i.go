func findMaxAverage(nums []int, k int) float64 {
    res, win, i := 0, 0, 0
    n := len(nums)

    for ; i < k; i++ {
        win += nums[i]
    }

    res = win

    for ; i < n; i++ {
        win += nums[i]
        win -= nums[i - k]

        res = max(res, win)
    }

    return float64(res) / float64(k)
}