import (
  "sort"
)

func minRemoval(nums []int, k int) int {
  sort.Ints(nums)   

  n := len(nums)
  left := 0
  minRem := n

  for right := range n {
    for nums[left] * k < nums[right] {
      left++
    }

    minRem = min(minRem, n - (right - left + 1))
  }

  return minRem
}