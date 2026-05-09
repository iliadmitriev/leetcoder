func maxUncrossedLines(nums1 []int, nums2 []int) int {

    dp := make(map[int][]int)

    for i, num := range nums2 {
        dp[num] = append(dp[num], i)
    }
    res := make([]int, 0, min(len(nums1), len(nums2)))

    for _, num := range nums1 {
        for i := len(dp[num]) - 1; i >= 0; i-- {
            idx := dp[num][i]

            j := bin_search(res, idx)
            if j == len(res) {
                res = append(res, idx)
            } else {
                res[j] = idx
            }
        }
    }

    return len(res)
}

func bin_search(arr []int, x int) int {
    lo, hi := 0, len(arr)
    for lo < hi {
        mid := (lo + hi) / 2
        if arr[mid] < x {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}