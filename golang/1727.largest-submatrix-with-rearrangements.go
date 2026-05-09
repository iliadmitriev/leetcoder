func largestSubmatrix(matrix [][]int) int {
  m, n := len(matrix), len(matrix[0])
  row := make([]int, n) // current heights
  maxArea := 0

  for i := range m { // O(m)

    // accumulate matrix vertically to get all the current heights
    for j := range n { // O(n)
      if matrix[i][j] == 0 {
        row[j] = 0 // reset on 0
      } else {
        row[j] += 1
      }
    }

    // sort heights
    sorted := make([]int, n)
    copy(sorted, row)
    sort.Ints(sorted) // O(n * log(n))

    // from highest to lowest
    for j := n - 1; j >= 0; j-- {
      width := n - j
      maxArea = max(maxArea, width * sorted[j])
    }
  }
    
  return maxArea
}