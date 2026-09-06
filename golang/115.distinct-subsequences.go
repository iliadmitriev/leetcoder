import (
  "strings"
  "fmt"
)

func numDistinct(s string, t string) int {
    // rebuild the source string s
    // with bytes than is only contained in t  
    // we don't need other characters
    var sb strings.Builder

    tt := make(map[byte]struct{})
    for j := range len(t) {
      tt[t[j]] = struct{}{}
    }

    for i := range len(s) {
      if _, ok := tt[s[i]]; ok {
        sb.WriteByte(s[i])
      }
    }

    // the new string
    ss := sb.String()

    m, n := len(ss), len(t)
    diff := m - n


    // if the source string length (less characters)
    // than the target, therefore it's impossible to
    // find any subsequence
    if diff < 0 {
      return 0
    }

    dp := make([]int, n + 1)
    dp[n] = 1 // base case

    for i := m - 1; i >= 0; i-- {
      start := max(0, i - diff) // bottom clipping 0
      end := min(n, i + 1) // top clipping n

      for j := start; j < end; j++ {
        if ss[i] == t[j] {
          dp[j] += dp[j + 1]
        }
      }
    }

    return dp[0]
}