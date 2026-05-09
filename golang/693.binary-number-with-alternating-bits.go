func hasAlternatingBits(n int) bool {
  prev := 1 ^ n & 1
  
  for ; n > 0; n >>= 1 {
    if n & 1 == prev {
      return false
    }
    
    prev = n & 1
  }

  return true
}