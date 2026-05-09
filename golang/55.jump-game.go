func canJump(nums []int) bool {
    n := len(nums)
    canJumpUpTo := 0

    for j := 0; j <= canJumpUpTo; j++ {

        if j == n - 1 {
            return true
        }

        if j + nums[j] > canJumpUpTo {
            canJumpUpTo = j + nums[j]
        }
    }

    return false
}