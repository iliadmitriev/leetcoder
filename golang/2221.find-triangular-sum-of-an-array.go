func triangularSum(nums []int) int {
    for i := len(nums); i >= 0; i-- {
        for j := 1; j < i; j++ {
            nums[j - 1] = (nums[j - 1] + nums[j]) % 10
        }
    }
    return nums[0]
}