func isTrionic(nums []int) bool {
  n := len(nums)
  p, q := 0, 0

  for i := 1; i < n - 1; i++ {
    if p == 0 && nums[i - 1] < nums[i] && nums[i] > nums[i + 1] {
      p = i
    } else if q == 0 && nums[i - 1] > nums[i] && nums[i] < nums[i + 1] {
      q = i
    } else if nums[i - 1] < nums[i] && nums[i] < nums[i + 1] {
      continue
    } else if nums[i - 1] > nums[i] && nums[i] > nums[i + 1] {
      continue
    } else {
      return false
    }
  } 

  return p > 0 && q > 0 && p < q
}