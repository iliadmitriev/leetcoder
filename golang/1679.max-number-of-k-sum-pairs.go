func maxOperations(nums []int, k int) int {

  sort.Ints(nums)

  op := 0

  for i, j := 0, len(nums) - 1; i < j; {
    s := nums[i] + nums[j]

    if s < k {
      i++
    } else if s > k {
      j--
    } else {
      op++
      i++
      j--
    }

  }

  return op
    
}