func largestInteger(nums []int, k int) int {
    n := len(nums)

    if n == k {
        return slices.Max(nums)
    }

    c := make(map[int]int)
    for _, x := range nums {
        c[x]++
    }

    if (k == 1) {
        mm := -1
        for _, x := range nums {
            if c[x] == 1 {
                mm = max(mm, x)
            }
        }
        return mm
    }

    c1, c2 := nums[0], nums[n-1]

    if c[c1] > 1 {
        c1 = -1
    }

    if c[c2] > 1 {
        c2 = -1
    }

    return max(c1, c2)
}