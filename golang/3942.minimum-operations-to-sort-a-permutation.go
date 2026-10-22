func minOperations(nums []int) int {
    n := len(nums)

    if n <= 1 {
        return 0
    }

    zero := slices.Index(nums, 0) // zero position (shift)
    asc, desc := true, true

    for i := 1; i < n; i++ {
        j := (zero + i) % n; // i-th value position

        if nums[j] != i {
            asc = false
        }

        if nums[j] != n - i {
            desc = false
        }

        if !asc && !desc {
            return -1
        }
    }

    if asc {
        return min(zero, n - zero + 2)
    }

    return min(n - zero, zero + 2)
}