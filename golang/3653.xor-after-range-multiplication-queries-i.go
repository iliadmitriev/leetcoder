func xorAfterQueries(nums []int, queries [][]int) int {
  const MOD = int(1e9) + 7

  applyQuery := func(l, r, k, v int) {
    for i := l ; i <= r; i += k {
      nums[i] *= v
      nums[i] %= MOD
    }
  }

  for _, q := range queries {
    applyQuery(q[0], q[1], q[2], q[3])
  }

  res := 0
  for _, num := range nums {
    res ^= num
  }

  return res
}