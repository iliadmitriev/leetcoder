func climbStairs(n int) int {
    p, c := 0, 1 // previous, current

    for range n {
      p, c = c, p + c
    }

    return c
}