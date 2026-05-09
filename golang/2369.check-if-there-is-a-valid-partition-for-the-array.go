func validPartition(nums []int) bool {
    n := len(nums)
    A, B, C := true, false, nums[0] == nums[1]

    for i := 2; i < n; i++{

        A, B, C = B, C, B && nums[i - 1] == nums[i] || A && ((nums[i - 2] == nums[i - 1] && nums[i - 1] == nums[i] ) || (nums[i - 2] + 1 == nums[i - 1] && nums[i - 1] + 1 == nums[i]))

    }

    return C
    
}