func reverseBits(n int) int {
  res := 0

  for range 32 {
    res <<= 1
    res |= n & 1
    n >>= 1
  }

  return res
}