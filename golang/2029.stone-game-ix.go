func stoneGameIX(stones []int) bool {
  c := [3]int{0, 0, 0}

  for _, s := range stones {
    c[s % 3]++
  }

  if c[0] % 2 == 0 {
    return c[1] >= 1 && c[2] >= 1
  }

  return c[1] - c[2] > 2 || c[2] - c[1] > 2
}