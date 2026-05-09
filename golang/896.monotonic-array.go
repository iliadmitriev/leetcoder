func isMonotonic(nums []int) bool {
    le, ge := true, true

    for i := 0; i < len(nums) - 1; i++ {
        if nums[i] < nums[i + 1] {
            ge = false
        }

        if nums[i] > nums[i + 1] {
            le = false
        }

        if !le && !ge {
            break
        }
    }

    return ge || le
}