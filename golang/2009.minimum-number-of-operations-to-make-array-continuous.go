func minOperations(nums []int) int {
    n := len(nums)
    // sort values
    sort.Ints(nums)
    // unique values
    j := 0
    for i := 0; i < n - 1; i++ {
        if nums[i] != nums[i + 1] {
            nums[j] = nums[i]
            j++
        }
    }
    nums[j] = nums[n - 1]
    j++
    nums = nums[:j]

    // sliding window
    left := 0
    window := 0
    maxWindow := 0

    for right := 0; right < len(nums); right++ {
        if nums[right] - nums[left] >= n {
            left++
        }
        window = right - left + 1
        if window > maxWindow {
            maxWindow = window
        }
    }
    return n - maxWindow
}