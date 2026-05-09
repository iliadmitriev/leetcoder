import (
    "math"
)


func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func minOperations(nums []int, x int) int {
    // sum all elements
    total := 0
    for _, num := range nums { total += num }

    target := total - x

    // optimization 1 (guard)
    if target < 0 {
        return -1
    }

    // optimization 2
    if target == 0 {
        return len(nums)
    }

    left := 0
    res := math.MaxInt
    currTotal := 0

    for right := 0; right < len(nums); right++ {
        // increase current total from right pointer
        currTotal += nums[right]

        // decrease current total from left pointer
        // but only if we exceeded the target
        for left <= right && currTotal > target {
            currTotal -= nums[left]
            left++
        }

        // if we able to collect target 
        // then check if it's minimal
        if currTotal == target {
            res = min(res, len(nums) - (right - left + 1))
        }
    }

    if res == math.MaxInt {
        return -1
    }
    return res
}