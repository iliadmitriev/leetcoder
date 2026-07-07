func sumAndMultiply(n int) int64 {
  nums := make([]int, 0)
  
  for ; n > 0; n /= 10 {
    if (n % 10 == 0) {
      continue
    }
    
    nums = append(nums, n % 10)
  }

  x := 0
  s := 0

  for len(nums) > 0 {
    d := nums[len(nums) - 1]
    nums = nums[:len(nums) - 1]

    x *= 10
    x += d
    s += d
  }

  return int64(s * x)
}