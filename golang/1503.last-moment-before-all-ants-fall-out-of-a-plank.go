func getLastMoment(n int, left []int, right []int) int {
    max_left := 0
    min_right := n

    for _, v := range left {
        if v > max_left {
            max_left = v
        }
    }

    for _, v := range right {
        if v < min_right {
            min_right = v
        }
    }

    if max_left > n - min_right {
        return max_left
    }
    return n - min_right
}