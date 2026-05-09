func jump(nums []int) int {
    n := len(nums)
    left, right := 0, 0
    jumps := 0

    for right < n - 1 {
        maxJump := 0
        for j := left; j <= right; j++ {
            if j + nums[j] > maxJump {
                maxJump = j + nums[j]
            }
        }
        left, right = right + 1, maxJump
        jumps++
    }

    return jumps
}