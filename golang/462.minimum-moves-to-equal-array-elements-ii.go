import (
    "slices"
)

func minMoves2(nums []int) int {
    n := len(nums)
    slices.Sort(nums)
    mid := nums[n / 2]

    abs := func(x int) int {
        if x < 0 {
            return -x
        }
        return x
    }

    res := 0

    for _, v := range nums {
        res += abs(mid - v)
    }

    return res
}