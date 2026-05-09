func minSwaps(grid [][]int) int {
  compress := func(row []int) int {
    n := len(row)
    for i := n - 1; i >= 0; i-- {
      if row[i] == 1 {
        return n - i - 1
      }
    }

    return n - 1
  }

  swaps := 0
  j := 0
  m := len(grid)
  rows := make([]int, m) // number of zeros starting from the right hand side

  for i, row := range grid {
    rows[i] = compress(row)
  }

  for i := range m {
    
    // if row doesn't have enough zeroes
    // look for closest replacement
    j = i
    for j < m && rows[j] < m - i - 1 {
      j++
    }

    // if replacement not found
    if j == m {
      return -1
    }

    // count swaps
    swaps += j - i

    // replace
    for ; j > i ; j-- {
      rows[j] = rows[j - 1]
    }
  }


  return swaps
}