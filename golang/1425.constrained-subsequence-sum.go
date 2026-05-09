func constrainedSubsetSum(nums []int, k int) int {
    // double ended queue with (index, value) tuples
    dq := make([]int, 0, len(nums))
    cache := make([]int, len(nums))
    cache[0] = nums[0]
    dq = append(dq, 0)
    out := nums[0]
    cur := 0

    for i := 1; i < len(nums); i++ {
        // drop all values from the left of the queue
        // which has indices less than window size
        // dq can't be empty: we add one value
        // from the start or previous iteration
        // and there always be previous value since k >= 1
        for i - dq[0] > k {
            dq = dq[1:]
        }
        
        // calcualte current value
        // and check if it's a new maximum
        cur = max(0, cache[dq[0]]) + nums[i]
        out = max(out, cur)

        // drop all values from the right of the queue
        // which is less or equal to current value
        // (queue could be empty)
        for len(dq) > 0 && cache[dq[len(dq) - 1]] <= cur {
            dq = dq[:len(dq) - 1]
        }
        dq = append(dq, i)
        cache[i] = cur
    }
    return out
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}