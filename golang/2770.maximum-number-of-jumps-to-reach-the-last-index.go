func maximumJumps(nums []int, target int) int {
  n := len(nums)
  dp := make([]int, n, n)
  for i := range dp {
    dp[i] = -1
  }

  dp[n - 1] = 0; // base case

  for j := n - 1; j >= 0; j-- {
    if dp[j] == -1 {
      continue // not connected
    }

    for i := j - 1; i >= 0; i-- {
      // if absolute difference greater than target => jump is not possible
      if max(nums[i] - nums[j], nums[j] - nums[i]) > target {
        continue
      }

      dp[i] = max(dp[i], dp[j] + 1)
    }
  }

  return dp[0];
}