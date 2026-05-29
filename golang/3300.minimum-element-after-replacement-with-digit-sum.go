func minElement(nums []int) int {
  digit := func(x int) int {
    sum := 0
    for ; x > 0; x /= 10 {
      sum += x % 10
    }

    return sum
  }

  cur := digit(nums[0])

  for _, x := range nums {
    cur = min(cur, digit(x))
  }
    
  return cur
}