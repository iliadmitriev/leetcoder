func minimumAbsDifference(arr []int) [][]int {
  ans := make([][]int, 0)

  sort.Ints(arr)

  minDiff := arr[1] - arr[0]

  for i := 1; i < len(arr); i++ {
    if arr[i] - arr[i - 1] < minDiff {
      ans = append(ans[:0], []int{arr[i - 1], arr[i]})
      minDiff = arr[i] - arr[i - 1]
    } else if arr[i] - arr[i - 1] == minDiff {
      ans = append(ans, []int{arr[i - 1], arr[i]})
    }
  }

  return ans    
}