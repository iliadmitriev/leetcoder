func bsearchRight(arr []int, x int) int {
    lo, hi := 0, len(arr)

    for lo < hi {
        mid := (lo + hi) / 2

        if arr[mid] <= x {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

func longestObstacleCourseAtEachPosition(obstacles []int) []int {
    n := len(obstacles)
    dp := make([]int, 0, n + 1)
    res := make([]int, n)

    for i, obs := range obstacles {
        if len(dp) == 0 || dp[len(dp) - 1] <= obs {
            dp = append(dp, obs)
            res[i] = len(dp)
        } else {
            j := bsearchRight(dp, obs)
            dp[j] = obs
            res[i] = j + 1
        }
    }
    return res
}