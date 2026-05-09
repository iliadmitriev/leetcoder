func findErrorNums(nums []int) []int {
    n := len(nums)
    // xor - both repeated and missing number
    xor := 0
    for i := 1; i <= n; i++ {
        xor ^= i ^ nums[i - 1]
    }

    // get different bit for repeated and missing numbers
    // (this could be a random not 0 bit, but I took the rightmost)
    rightmost := xor & ^(xor - 1)

    // separate repeated and missing number with different bit
    xor0, xor1 := 0, 0
    for i := 1; i <= n; i++ {
        if rightmost & nums[i - 1] > 0 {
            xor0 ^= nums[i - 1]
        } else {
            xor1 ^= nums[i - 1]
        }

        if rightmost & i > 0 {
            xor0 ^= i
        } else {
            xor1 ^= i
        }
    }

    // if xor0 present in original set it's repeated number and xor1 is missing
    for _, num := range nums {
        if xor0 == num {
            return []int{xor0, xor1}
        }
    }

    // otherwise
    return []int{xor1, xor0}
}