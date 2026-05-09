func binaryGap(n int) int {
  gap := 0
  maxGap := 0

  for ; n > 0 && n & 1 == 0; n >>= 1 {}

  for ; n > 0; n >>= 1 {
    if n & 1 == 0 {
      gap++
    } else {
      maxGap = max(maxGap, gap)
      gap = 1
    }
  }

  return maxGap
}