func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []bool {
  group := 0
  groups := make([]int, n)
  res := make([]bool, len(queries))

  for i := 1; i < n; i++ {
    if nums[i] - nums[i - 1] > maxDiff {
      group++
    }

    groups[i] = group
  }
  
  for j, q := range queries {
    u, v := q[0], q[1]
    res[j] = groups[u] == groups[v]
  }

  return res
}