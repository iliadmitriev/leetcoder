func dp(p1 int, p2 int, nums[]int) bool {
    n := len(nums)
    if n == 0 {
        return p1 >= p2
    } else if n == 1 {
        return nums[0] + p1 >= p2
    }

    return (dp(p1 + nums[0], p2 + nums[n-1], nums[1:n-1]) && dp(p1 + nums[0], p2 + nums[1], nums[2:])) || 
        (dp(p1 + nums[n-1], p2 + nums[0], nums[1:n-1]) && dp(p1 + nums[n-1], p2 + nums[n-2], nums[:n-2]))
    
}


func PredictTheWinner(nums []int) bool {

    return dp(0, 0, nums)

}