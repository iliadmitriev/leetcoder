func minFlips(s string) int {
	parity := "01"
	n := len(s)
  count := 0

	for i := range n {

		if s[i] == parity[i%2] {
			count++
		} 
	}

	res := min(count, n - count)

	if n%2 == 0 {
		return res
	}


  for i := range n {
    if s[i] == parity[i%2] {
      count--
    }

    if s[i] == parity[(i + 1) % 2] {
      count++
    }

    res = min(res, min(count, n - count))
  }

	return res
}