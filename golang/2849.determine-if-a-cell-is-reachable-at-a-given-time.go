func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
    if fx == sx && fy == sy {
        return t != 1
    }
    dx, dy := abs(fx - sx), abs(fy - sy)
    return t >= max(dx, dy)
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func max(values ...int) int {
    maxValue := values[0]
    for _, v := range values {
        if v > maxValue {
            maxValue = v
        }
    }
    return maxValue
}