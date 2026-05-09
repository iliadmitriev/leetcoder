func longestSubarray(nums []int) int {

    maxLen := 0
    zeros := 0

    n := len(nums)

    for i, j := 0, 0; i < n; i++ {
        if nums[i] == 0 {
            zeros++
        }

        for zeros > 1 {
            if nums[j] == 0 {
                zeros--
            }
            j++
        }

        maxLen = max(maxLen, i - j)
    }

    return maxLen
}