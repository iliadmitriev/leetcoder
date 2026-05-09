import (
    "sort"
)

func maxFrequency(nums []int, k int) int {
    budget := k
    n := len(nums)
    sort.Ints(nums)

    l, r := 0, 0
    res := 0

    for ; r < n; r++ {
        budget += nums[r]

        if !(budget >= nums[r] * (r - l + 1)) {
            budget -= nums[l]
            l++
        }

        if res < r - l + 1 {
            res = r - l + 1
        }
    }

    return res
}