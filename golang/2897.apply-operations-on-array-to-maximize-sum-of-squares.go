func maxSum(nums []int, k int) int {
	const SIZE = 30
	const MOD = int(1e9) + 7

	res := 0
	bits := [SIZE]int{0}

	for _, num := range nums {
		for i := range SIZE {
			if num&(1<<i) > 0 {
				bits[i]++
			}
		}
	}

  for range k {
    v := 0
    for i := SIZE - 1; i >= 0; i-- {
      if bits[i] > 0 {
        bits[i]--
        v |= 1 << i
      }
    }

    res = (res + v * v) % MOD
  }

	return res
}