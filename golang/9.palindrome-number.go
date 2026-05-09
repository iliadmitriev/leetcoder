func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

  bwd, fwd := x, 0

  for x > 0 {
    fwd = fwd * 10 + x % 10
    x /= 10
  }

  return fwd == bwd
}