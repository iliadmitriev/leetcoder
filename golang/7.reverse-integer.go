func reverse(x int) int {
	sign := x < 0
	if sign {
		x = -x
	}

	res := 0
	for x > 0 {
		res = res*10 + x%10
		x /= 10
	}

	if sign {
		res = -res
	}

  if res < -(1<<31) || (1<<31) - 1 < res {
    return 0
  }

	return res
}