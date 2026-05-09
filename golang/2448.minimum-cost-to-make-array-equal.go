func minCost(nums []int, cost []int) int64 {
    cache := make(map[int]int64)
    getCost := func(base int) int64 {
        if val, ok := cache[base]; ok {
            return val
        }
        n := len(nums)
        var res int64 = 0
        for i := 0; i < n; i++ {
            res += int64(cost[i]) * int64(abs(nums[i] - base))
        }
        cache[base] = res;
        return res
    }

    lo, hi := min(nums), max(nums)
    for lo < hi {
        mid := (lo + hi) / 2
        if getCost(mid) > getCost(mid + 1) {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return getCost(lo)
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func min(arr []int) int {
    res := arr[0]
    for _, v := range arr {
        if v < res {
            res = v
        }
    }
    return res
}

func max(arr []int) int {
    res := arr[0]
    for _, v := range arr {
        if v > res {
            res = v
        }
    }
    return res
}