func findThePrefixCommonArray(A []int, B []int) []int {

  n := len(A)
  cache := make([]int, n + 1)

  res := make([]int, n)
  cur := 0

  for i := range n {
    a, b := A[i], B[i]

    cache[a]++
    if cache[a] == 2 {
      cur++
    }

    cache[b]++
    if cache[b] == 2 {
      cur++
    }

    res[i] = cur
  } 

  return res   
}