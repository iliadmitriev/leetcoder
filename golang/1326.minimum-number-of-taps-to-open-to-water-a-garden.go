func minTaps(n int, ranges []int) int { 
    maxRanges := make([]int, n + 1)
    for i := 0; i < n + 1; i++ {
        start, end := max(0, i - ranges[i]), min(n, i + ranges[i])
        maxRanges[start] = max(maxRanges[start], end)
    }

    taps := 0
    maxEnd, curEnd := 0, 0

    for i := 0; i < n + 1; i++ {
        if maxEnd < i {
            return -1
        }

        if curEnd < i {
            curEnd = maxEnd
            taps++
        }

        if maxEnd < maxRanges[i] {
            maxEnd = maxRanges[i]
        }
    }
    return taps
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}