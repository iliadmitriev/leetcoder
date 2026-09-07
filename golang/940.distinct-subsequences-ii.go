func distinctSubseqII(s string) int {
    const (
      base = byte('a')
      mod = int(1e9) + 7
    )

    dp := 1
    prev := dp
    last := make([]int, 26)

    for i := range len(s) {
      prev = dp
      dp *= 2
      
      j := s[i] - base
      dp += mod - last[j]
      dp %= mod

      last[j] = prev
    }

    return (dp + mod - 1) % mod
}