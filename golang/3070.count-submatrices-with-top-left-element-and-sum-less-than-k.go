func countSubmatrices(grid [][]int, k int) int {
  m, n := len(grid), len(grid[0])
  count := 0
  row := make([]int, n)

  for i := range m {
    cur := 0
    for j := range n {
      row[j] += grid[i][j]
      cur += row[j]

      if cur <= k {
        count++
      } else {
        break
      }
    }

  }

  return count
}