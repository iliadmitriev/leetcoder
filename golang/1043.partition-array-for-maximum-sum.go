
func maxSumAfterPartitioning(arr []int, k int) int {
    n := len(arr)
    cache := make([]int, n)
    for i := range cache { cache[i] = -1 }

    var dp func(int) int
    dp = func (i int) int {
        if i >= len(arr) {
            return 0
        }

        if cache[i] != -1 {
            return cache[i]
        }

        res := 0
        curMax := 0

        for j := i; j < minInt(i + k, n); j++ {
            rec := dp(j + 1)
            curMax = maxInt(curMax, arr[j])
            v := curMax * (j - i + 1) + rec
            res = maxInt(res, v)
        }

        cache[i] = res
        return res
    }

    return dp(0)
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func maxInt(a, b int) int {
    if a > b { 
        return a
    }
    return b
}
