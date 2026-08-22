func checkDivisibility(n int) bool {
  var d int
  
  p, s := 1, 0

  for x := n; x > 0; x /= 10 {
    d = x % 10
    p *= d
    s += d
  }

  return n % (s + p) == 0
}