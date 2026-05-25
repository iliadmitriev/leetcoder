func canReach(s string, minJump int, maxJump int) bool {
    n := len(s)
    if s[0] == '1' || s[n - 1] == '1' {
      return false
    }

    dp := make([]int, n)

    if minJump < n {
      dp[minJump]++
    }

    if maxJump + 1 < n {
      dp[maxJump + 1]--
    }

    for i := 1; i < n; i++ {
      dp[i] += dp[i - 1]

      // if there is no way or lost connection
      if s[i] == '1' || dp[i] == 0 {
        continue
      }

      // from min jump
      if i + minJump < n {
        dp[i + minJump]++
      }

      // to max jump
      if i + maxJump + 1 < n {
        dp[i + maxJump + 1]--
      }
    }

    return dp[n - 1] > 0
}