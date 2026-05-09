func trap(height []int) int {
	n := len(height)
  trapped := 0
  st := make([]int, 0, n)

  for i := range n {
    for len(st) > 0 && height[i] > height[st[len(st) - 1]] {
      prev := st[len(st) - 1]
      st = st[:len(st) - 1]

      // calc trapped
      if len(st) > 0 {
        left := height[st[len(st) - 1]]
        edges := min(left, height[i])
        bottom := height[prev]
        h := edges - bottom // >= 0
        w := i - st[len(st) - 1] - 1

        trapped += h * w
      }
    }

    st = append(st, i)
  }

  return trapped
}